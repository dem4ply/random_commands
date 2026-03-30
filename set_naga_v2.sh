#!/bin/bash

# usar `xev` para ver las codigos de las teclas

# sacados de muchos lugares
# /usr/include/X11/keysymdef.h
# /usr/share/X11/xkb/keycodes/digital_vndr/pc
#
mkdir -p /tmp/xkb/symbols/
cat >/tmp/xkb/symbols/custom <<\EOF
xkb_symbols "remote" {
    key <AE12>   {      [0x0031]       };
    key <AE07>   {      [0x0032]       };
    key <AE08>   {      [0x0033]       };

    key <AE09>   {      [0x0034]       };
    key <AE10>   {      [0x0035]       };
    key <AE11>   {      [0x0036]       };

    key <FK01>   {      [0x0037]       };
    key <FK02>   {      [0x0038]       };
    key <FK03>   {      [0x0039]       };

    key <FK04>   {      [0x0030]       };
    key <FK05>   {      [0x002d]       };
    key <FK06>   {      [0x003d]       };
};
EOF

cat /tmp/xkb/symbols/custom

remote_ids=$( xinput list | sed -n 's/.*Naga V2.*id=\([0-9]*\).*keyboard.*/\1/p' )

for id in $remote_ids; do
	echo "cambiando input:"
	xinput list | grep -i $id;

	echo "antes:"
	setxkbmap -device $id -print

	echo "despues:"
	setxkbmap -device $id -print \
	| sed 's/\(xkb_symbols.*pc+latam+us\)\(.*\)"/\1+custom(remote)\2"/'

	setxkbmap -device $id -print \
	| sed 's/\(xkb_symbols.*pc+latam+us\)\(.*\)"/\1+custom(remote)\2"/' \
	| xkbcomp -I/tmp/xkb -i $id -synch - $DISPLAY 2> /dev/null;
done;
