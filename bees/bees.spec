%global sha     fd6c3b37698f1578251acac255ccd58697689a8b
Name:           bees
Version:        2023.1.28
Release:        1%{?dist}
Summary:        Best-Effort Extent-Same, a btrfs dedup agent

License:        GPL3
URL:            https://github.com/Zygo/bees
Source0:        https://github.com/Zygo/bees/archive/%{sha}.zip

BuildRequires:  make automake gcc gcc-c++ kernel-devel discount libuuid-devel btrfs-progs-devel
Requires:       libuuid btrfs-progs

Patch0001:      0001-build-optimizations.patch

%description


%prep
%autosetup -p1 -n bees-%{sha}


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
export BEES_VERSION=%{version}
export SYSTEMD_SYSTEM_UNIT_DIR=/usr/lib/systemd/system
%make_install


%files
/usr/sbin/beesd
/usr/lib/bees/bees
/etc/bees/beesd.conf.sample
/usr/lib/systemd/system/beesd@.service


%changelog
* Tue Feb 14 2023 Piotr Rogowski <piotrekrogowski@gmail.com> - 2023.1.28-1
- new version

* Mon Nov 14 2022 Piotr Rogowski <piotrekrogowski@gmail.com> - 2022.11.5-1
- new version

* Fri Apr 15 2022 Piotr Rogowski <piotrekrogowski@gmail.com> - 2021.12.19-1
- new version

* Fri Nov 26 2021 Piotr Rogowski <piotrekrogowski@gmail.com> - 2021.11.1-1
- new version

* Mon Jun 28 2021 Piotr Rogowski <piotrekrogowski@gmail.com> - 2021.09.19-1
- new version

* Fri Mar 26 2021 Piotr Rogowski <piotrekrogowski@gmail.com> - 2021.02.23-1
- new version

* Tue Nov 24 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 2020.10.10-1
- Update version

* Fri Jan 24 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 2019.11.28-2
- rebuilt

* Fri Jan 24 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl>
-
