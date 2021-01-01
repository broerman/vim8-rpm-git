Name:		vim
Version:	8.2
Release:	2230%{?dist}
Summary:	The VIM editor

License:	Vim and MIT
URL:		https://github.com/vim/vim.git

BuildRequires: hunspell-devel
BuildRequires: gcc
BuildRequires: python2-devel python3-devel ncurses-devel gettext perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::Embed) perl(ExtUtils::ParseXS)
BuildRequires: libacl-devel gpm-devel autoconf file
BuildRequires: libappstream-glib
BuildRequires: libselinux-devel
BuildRequires: ruby-devel ruby
BuildRequires: lua-devel
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: libSM-devel
BuildRequires: libXt-devel
BuildRequires: libXpm-devel
BuildRequires: libICE-devel

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%prep
rm -rf vim
git clone --depth=1 %{url} vim
cd vim

%build
cd vim
%configure --with-features=huge --with-x=no \
  --prefix=/usr/local \
  --exec-prefix=/usr/local \
  --bindir=/usr/local/bin \
  --enable-multibyte \
  --disable-netbeans \
  --disable-selinux \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm \
  --with-compiledby="Bernd Broermann <bernd@broermann.com>" \
  --with-modified-by="Bernd Broermann <bernd@broermann.com>"

make %{?_smp_mflags}

%install
cd vim
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/share
make install DESTDIR=%{buildroot}

# avoid conflicts when installing with distro vi
rm -rf %{buildroot}/usr/share/man
rm -rf %{buildroot}/usr/share/applications
rm -rf %{buildroot}/usr/share/icons

rm -f %{buildroot}/usr/local/bin/ex
rm -f %{buildroot}/usr/local/bin/rvim
rm -f %{buildroot}/usr/local/bin/view
rm -f %{buildroot}/usr/local/bin/rview
rm -f %{buildroot}/usr/local/bin/vimdiff
rm -f %{buildroot}/usr/local/bin/vimtutor

%files
/usr/local/bin/*
/usr/share/*
%doc

%changelog
* Sun Dec 27 2020 Bernd Broermann <bernd@broermann.com>
  Initial vim package

