%global ututorelnum 11
%global relnum 40
%global Bg_Name UTUTO
%global bgname %(t="%{Bg_Name}";echo ${t,,})

# Enable Extras
%global with_extras 1

Name:           %{bgname}-backgrounds
Version:        %{relnum}.2.0
Release:        %autorelease
Summary:        Ututo %{ututorelnum} default desktop background

License:        CC-BY-SA-4.0
URL:            https://ututo.ar
Source0:        https://github.com/ututolinux/ututo-packages/releases/download/v0.2.0-alpha/ututo-backgrounds-11.tar.xz


BuildArch:      noarch

BuildRequires:  make

Requires:       %{name}-budgie = %{version}-%{release}
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Ututo  %{ututorelnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Ututo  %{ututorelnum} default background
License:        CC-BY-SA-4.0

%description    base
This package contains base images for Ututo  %{ututorelnum} default background.

%package        budgie
Summary:        Ututo  %{ututorelnum} default wallpaper for Budgie
Requires:       %{name}-base = %{version}-%{release}
Recommends:	    %{name}-gnome = %{version}-%{release}

%description    budgie
This package contains Budgie desktop wallpaper for the
Ututo  %{ututorelnum} default theme.

%package        gnome
Summary:        Ututo  %{ututorelnum} default wallpaper for Gnome and Cinnamon
Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Ututo  %{ututorelnum} default theme.

%package        mate
Summary:        Ututo %{ututorelnum} default wallpaper for Mate
Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for Ututo  %{ututorelnum}
default theme.

%package        xfce
Summary:        Ututo  %{ututorelnum} default background for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop background for the Ututo  %{ututorelnum}
default theme.

%if %{with_extras}
%package        extras-base
Summary:        Base images for  Extras Backgrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-base
This package contains base images for  supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra  Wallpapers for Gnome and Cinnamon

Requires:       %{name}-extras-base = %{version}-%{release}

%description    extras-gnome
This package contains  supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra  Wallpapers for Mate

Requires:       %{name}-extras-base = %{version}-%{release}

%description    extras-mate
This package contains  supplemental wallpapers for Mate

%package        extras-xfce
Summary:        Extra  Wallpapers for XFCE

Requires:       %{name}-extras-base = %{version}-%{release}

%description    extras-xfce
This package contains  supplemental wallpapers for XFCE
%endif

%prep
%autosetup -n %{name}


%build
%make_build


%install
%make_install

%files
%doc

%files base
%license COPYING Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}*.{png,xml}

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml
%dir %{_datadir}/gnome-background-properties/

%files budgie
%{_datadir}/gnome-background-properties/%{bgname}-budgie.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml
%dir %{_datadir}/mate-background-properties/

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png
%dir %{_datadir}/xfce4/
%dir %{_datadir}/xfce4/backdrops/

%if %{with_extras}
%files extras-base
%license COPYING
%{_datadir}/backgrounds/%{bgname}/extras/

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/
%endif

%changelog
%autochangelog
