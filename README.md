
# Este es el repositorio de paquetes personalizados

## Pasos para el build , por ejemplo de *generic-release* :
```
cd generic-release

fedpkg mockbuild
```

## Pasos para la instalación:
```
sudo dnf5 install results_generic-release/40/0.2/generic-release-40-0.2.noarch.rpm results_generic-release/40/0.2/generic-release-common-40-0.2.noarch.rpm --allowerasing
```


