#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-snappy-java
Version  : 1.1.7.1
Release  : 5
URL      : https://github.com/xerial/snappy-java/archive/1.1.7.1.tar.gz
Source0  : https://github.com/xerial/snappy-java/archive/1.1.7.1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.0.4.1/snappy-java-1.0.4.1.jar
Source2  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.0.4.1/snappy-java-1.0.4.1.pom
Source3  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.0.5/snappy-java-1.0.5.jar
Source4  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.0.5/snappy-java-1.0.5.pom
Source5  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.1.3/snappy-java-1.1.1.3.jar
Source6  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.1.3/snappy-java-1.1.1.3.pom
Source7  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.4/snappy-java-1.1.4.jar
Source8  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.4/snappy-java-1.1.4.pom
Source9  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.7.1/snappy-java-1.1.7.1.jar
Source10  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.7.1/snappy-java-1.1.7.1.pom
Source11  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.7.3/snappy-java-1.1.7.3.jar
Source12  : https://repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.7.3/snappy-java-1.1.7.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: mvn-snappy-java-data = %{version}-%{release}
Requires: mvn-snappy-java-license = %{version}-%{release}

%description
This folder contains the native libraries built for various platforms.

%package data
Summary: data components for the mvn-snappy-java package.
Group: Data

%description data
data components for the mvn-snappy-java package.


%package license
Summary: license components for the mvn-snappy-java package.
Group: Default

%description license
license components for the mvn-snappy-java package.


%prep
%setup -q -n snappy-java-1.1.7.1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-snappy-java
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-snappy-java/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-snappy-java/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.4.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.4.1/snappy-java-1.0.4.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.4.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.4.1/snappy-java-1.0.4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.5/snappy-java-1.0.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.5/snappy-java-1.0.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.1.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.1.3/snappy-java-1.1.1.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.1.3
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.1.3/snappy-java-1.1.1.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.4
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.4/snappy-java-1.1.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.4
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.4/snappy-java-1.1.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.1/snappy-java-1.1.7.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.1/snappy-java-1.1.7.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.3
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.3/snappy-java-1.1.7.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.3
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.3/snappy-java-1.1.7.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.4.1/snappy-java-1.0.4.1.jar
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.4.1/snappy-java-1.0.4.1.pom
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.5/snappy-java-1.0.5.jar
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.0.5/snappy-java-1.0.5.pom
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.1.3/snappy-java-1.1.1.3.jar
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.1.3/snappy-java-1.1.1.3.pom
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.4/snappy-java-1.1.4.jar
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.4/snappy-java-1.1.4.pom
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.1/snappy-java-1.1.7.1.jar
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.1/snappy-java-1.1.7.1.pom
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.3/snappy-java-1.1.7.3.jar
/usr/share/java/.m2/repository/org/xerial/snappy/snappy-java/1.1.7.3/snappy-java-1.1.7.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-snappy-java/LICENSE
/usr/share/package-licenses/mvn-snappy-java/NOTICE
