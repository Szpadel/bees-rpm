Name:           bees
Version:        2019.11.28
Release:        1%{?dist}
Summary:        Best-Effort Extent-Same, a btrfs dedup agent

License:        GPL3
URL:            https://github.com/Zygo/bees
Source0:        https://github.com/Zygo/bees/archive/07e5e7bd1b348eb2d56bc2a7974c3a660081418a.zip

BuildRequires:  discount libuuid-devel btrfs-progs-devel
Requires:       libuuid btrfs-progs

Patch0001:      0001-build-optimizations.patch

%description


%prep
cd bees-*
%autopatch -p1
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files



%changelog
* Fri Jan 24 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl>
- 