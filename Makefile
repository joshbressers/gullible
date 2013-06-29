# Copyright 2013 Josh Bressers <bressers@redhat.com>
#
# This file is part of gullible.
# 
# gullible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# gullible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with gullible.  If not, see <http://www.gnu.org/licenses/>.

PKGNAME=gullible

PREFIX=/usr
BINDIR=${PREFIX}/bin
DATADIR=${PREFIX}/share

# We need to figure out a nice way to do this on 32 and 64 archs
GDBDIR=${DATADIR}/gdb/python/gdb/command

PKGDATADIR=${DATADIR}/${PKGNAME}

all:
# Do nothing

test:
# Do nothing

install: all
		mkdir -p $(DESTDIR)$(BINDIR)
		mkdir -p $(DESTDIR)$(PKGDATADIR)/gullible
		mkdir -p $(DESTDIR)$(GDBDIR)

		# This is all a terrible hack, we'll need to figure out how to do it right

		install -m 0755 bin/gullible.sh $(DESTDIR)$(BINDIR)/gullible
		install -m 0644 README.txt $(DESTDIR)$(PKGDATADIR)
		install -m 0644 COPYING $(DESTDIR)$(PKGDATADIR)
		install -m 0644 lib/gullible/*.py -t $(DESTDIR)$(PKGDATADIR)/gullible/

		# Is there a better way to do this?
		install -m 0644 gdb/gullible.py $(DESTDIR)$(GDBDIR)/
		echo "import sys; sys.path.append('$(PKGDATADIR)')" > $(DESTDIR)$(GDBDIR)/gullible.py
		cat gdb/gullible.py >> $(DESTDIR)$(GDBDIR)/gullible.py
