%global upstreamname HIPIFY

%global rocm_release 5.7
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# This is a clang tool so best to build with clang
%global toolchain clang

Name:           hipify
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        Convert CUDA to HIP

Url:            https://github.com/ROCm-Developer-Tools
License:        BSD-3-Clause
Source0:        %{url}/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-prepare-hipify-cmake-for-fedora.patch

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  glibc-headers
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  zlib-devel

# ROCm is really only on x86_64
ExclusiveArch:  x86_64

%description
HIPIFY is a set of tools to translate CUDA source code into portable
HIP C++ automatically.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/usr/hip

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/findcode.sh
%{_bindir}/finduncodep.sh
%{_bindir}/hipconvertinplace-perl.sh
%{_bindir}/hipconvertinplace.sh
%{_bindir}/hipexamine-perl.sh
%{_bindir}/hipexamine.sh
%{_bindir}/hipify-clang
%{_bindir}/hipify-perl

%changelog
* Sun Oct 1 2023 Tom Rix <trix@redhat.com> - 5.7.0-1
- Initial package
