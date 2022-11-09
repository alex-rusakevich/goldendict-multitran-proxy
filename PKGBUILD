# Maintainer: Your Name <mr.alexander.rusakevich@gmail.com>
pkgname="goldendict-multitran-proxy"
pkgver="0.1"
pkgrel=1
epoch=
pkgdesc="Local proxy to be used with Golden Dict in order to add Multitran support"
arch=("i686" "x86_64")
url=""
license=('GPL3')
groups=()
depends=("python>=3.10")
makedepends=("python-pip>=22" "git")
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("$pkgname"::"git+https://github.com/alex-rusakevich/goldendict-multitran-proxy")
noextract=()
md5sums=("skip")
validpgpkeys=()

build() {
	cd "$pkgname"
	make
}

package() {
	cd "$pkgname"
	make DESTDIR="$pkgdir/usr/share/$pkgname" install
}
