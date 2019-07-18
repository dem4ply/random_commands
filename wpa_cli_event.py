#!/usr/bin/env python3

import sys
from datetime import datetime

from chibi.file import Chibi_file, Chibi_path


path = Chibi_path( __file__ )

f = Chibi_file( ( path + "wpa_cli" ) + "wpa_cli" )
date = datetime.utcnow()

event = ",".join( sys.argv[1:] )

final_even = "{}\t{}\n".format( date.isoformat(), event )

f.append( final_even )
