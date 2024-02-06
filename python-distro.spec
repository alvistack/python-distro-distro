# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-distro
Epoch: 100
Version: 1.8.0
Release: 1%{?dist}
BuildArch: noarch
Summary: OS platform information API
License: Apache-2.0
URL: https://github.com/python-distro/distro/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
distro provides information about the OS distribution it runs on, such
as a reliable machine-readable ID, or version information.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-distro
Summary: OS platform information API
Requires: python3
Provides: python3-distro = %{epoch}:%{version}-%{release}
Provides: python3dist(distro) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-distro = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(distro) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-distro = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(distro) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-distro
distro provides information about the OS distribution it runs on, such
as a reliable machine-readable ID, or version information.

%files -n python%{python3_version_nodots}-distro
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-distro
Summary: OS platform information API
Requires: python3
Provides: python3-distro = %{epoch}:%{version}-%{release}
Provides: python3dist(distro) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-distro = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(distro) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-distro = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(distro) = %{epoch}:%{version}-%{release}

%description -n python3-distro
distro provides information about the OS distribution it runs on, such
as a reliable machine-readable ID, or version information.

%files -n python3-distro
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
