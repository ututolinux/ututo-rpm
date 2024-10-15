Summary:        Ututo package repositories
Name:           ututo-repos
Version:        40
Release:        2
License:        MIT
URL:            https://ututo.ar/

Provides:       ututo-repos(%{version}) = %{release}
Requires:       ututo-release
BuildArch:      noarch
# Required by %%check
BuildRequires:  sed rpm

Source1:        ututo.repo


%description
Ututo package repository files for yum and dnf.


%prep

%build

%install

# Install repo files
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in %{_sourcedir}/ututo*repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done

%check
# Make sure all repo variables were substituted
for repo in $RPM_BUILD_ROOT/etc/yum.repos.d/*.repo; do
    if grep -q AUTO_VALUE $repo; then
        echo "ERROR: Repo $repo contains an unsubstituted placeholder value"
        exit 1
    fi
done


# Make sure metadata_expire was correctly set
%if "%{release}" < "1"
expire_value='6h'
%else
expire_value='7d'
%endif
for repo in $RPM_BUILD_ROOT/etc/yum.repos.d/ututo.repo; do
    lines=$(grep '^metadata_expire=' $repo | sort | uniq)
    if [ "$(echo "$lines" | wc -l)" -ne 1 ]; then
        echo "ERROR: Non-matching metadata_expire lines in $repo: $lines"
        exit 1
    fi
    if test "$lines" != "metadata_expire=${expire_value}"; then
        echo "ERROR: Wrong metadata_expire value in $repo: $lines"
        exit 1
    fi
done


%files
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/ututo.repo


%changelog
* Tue Oct 12 2024 Guillermo Joandet <gjoandet@gmail.com> - 40-1
- Change repository location

* Sat Oct 12 2024 Guillermo Joandet <gjoandet@gmail.com> - 40-1
- Initial version
