Summary:	A catchy.net initiative to deliver a full-featured WAP browser
Summary(pl):	Inicjatywa catchy.net, by dostarczyæ przegl±darkê WAP o pe³nych mo¿liwo¶ciach
Name:		mobilizer
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://unc.dl.sourceforge.net/sourceforge/mobilizer/mobilizer-0.2.3.tar.gz
# Source0-md5:	b621a0996c975a150afbe2488cb2a7fb
Patch0:		%{name}-glade.patch
URL:		http://mobilizer.sourceforge.net/
BuildRequires:	ORBit-devel >= 0.5.0
BuildRequires:	doxygen
BuildRequires:	gnome-core-devel >= 1.2.0
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	libglade-gnome-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
A catchy.net initiative to deliver a full-featured WAP browser.

%description -l pl
Inicjatywa catchy.net, by dostarczyæ przegl±darkê WAP o pe³nych
mo¿liwo¶ciach.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
CPPFLAGS="`libglade-config --cflags`"; export CPPFLAGS
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install source/app/unix/*.glade $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
