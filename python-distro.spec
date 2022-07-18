%global debug_package %{nil}

Name: python-distro
Epoch: 100
Version: 1.6.0
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

%if 0%{?suse_version} > 1500
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

%if !(0%{?suse_version} > 1500)
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
