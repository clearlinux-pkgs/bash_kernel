Name     : bash_kernel
Version  : 0.4.1
Release  : 1
URL      : https://github.com/takluyver/bash_kernel/releases/download/0.4.1/bash_kernel-0.4.1-py2.py3-none-any.whl
Source0  : https://github.com/takluyver/bash_kernel/releases/download/0.4.1/bash_kernel-0.4.1-py2.py3-none-any.whl
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : python3-dev
BuildRequires : pip

%description
No detailed description available

%prep

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486351168

%install
rm -rf %{buildroot}
pip3 install --no-deps  --root %{buildroot} %{SOURCE0}
for i in `find %{buildroot} -name "*.so" `; do rm $i; done


%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages
