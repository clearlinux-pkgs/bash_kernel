Name     : bash_kernel
Version  : 0.4.1
Release  : 11
URL      : https://github.com/takluyver/bash_kernel/releases/download/0.4.1/bash_kernel-0.4.1-py2.py3-none-any.whl
Source0  : https://github.com/takluyver/bash_kernel/releases/download/0.4.1/bash_kernel-0.4.1-py2.py3-none-any.whl
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : python3-dev
BuildRequires : pip
BuildRequires : pyzmq
BuildRequires : ipykernel
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : python-dateutil
BuildRequires : pexpect
BuildRequires : ptyprocess
BuildRequires : wcwidth

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


python3 %{buildroot}/usr/lib/python$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_version())")/site-packages/bash_kernel/install.py  install --prefix %{buildroot}/usr
%files
%defattr(-,root,root,-)
/usr/lib/python3*/site-packages
