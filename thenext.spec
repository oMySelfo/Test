Name: The_next
Version: 1
Release: 1
Summary: The package for APPLICATION.
Group: The_next
License: internal
Source: /var/lib/jenkins/workspace/Thenext/Address2/target/Address2.war


BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: x86_64

%description
Test build RPM

%prep

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/apptest/
cp ../var/lib/jenkins/workspace/Thenext/Address2/target/Address2.war %{buildroot}/apptest/Address2.war

%clean
rm -rf %{buildroot}



%changelog
- Initial build.