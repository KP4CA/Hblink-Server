'''
THIS EXAMPLE WILL NOT WORK AS IT IS - YOU MUST SPECIFY YOUR OWN VALUES!!!

This file is organized around the "Conference Bridges" that you wish to use. If you're a c-Bridge
person, think of these as "bridge groups". You might also liken them to a "reflector". If a particular
system is "ACTIVE" on a particular conference bridge, any traffid from that system will be sent
to any other system that is active on the bridge as well. This is not an "end to end" method, because
each system must independently be activated on the bridge.

The first level (e.g. "WORLDWIDE" or "STATEWIDE" in the examples) is the name of the conference
bridge. This is any arbitrary ASCII text string you want to use. Under each conference bridge
definition are the following items -- one line for each HBSystem as defined in the main HBlink
configuration file.

    * SYSTEM - The name of the sytem as listed in the main hblink configuration file (e.g. hblink.cfg)
        This MUST be the exact same name as in the main config file!!!
    * TS - Timeslot used for matching traffic to this confernce bridge
        XLX connections should *ALWAYS* use TS 2 only.
    * TGID - Talkgroup ID used for matching traffic to this conference bridge
        XLX connections should *ALWAYS* use TG 9 only.
    * ON and OFF are LISTS of Talkgroup IDs used to trigger this system off and on. Even if you
        only want one (as shown in the ON example), it has to be in list format. None can be
        handled with an empty list, such as " 'ON': [] ".
    * TO_TYPE is timeout type. If you want to use timers, ON means when it's turned on, it will
        turn off afer the timout period and OFF means it will turn back on after the timout
        period. If you don't want to use timers, set it to anything else, but 'NONE' might be
        a good value for documentation!
    * TIMOUT is a value in minutes for the timout timer. No, I won't make it 'seconds', so don't
        ask. Timers are performance "expense".
    * RESET is a list of Talkgroup IDs that, in addition to the ON and OFF lists will cause a running
        timer to be reset. This is useful   if you are using different TGIDs for voice traffic than
        triggering. If you are not, there is NO NEED to use this feature.
'''

BRIDGES = {
    'Boriken DMR Net': [
            {'SYSTEM': 'BORIKEN DMR NET MASTER',    'TS': 2, 'TGID': 4630,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4630], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 1, 'TGID': 4630,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4630], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 1, 'TGID': 4630,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4630], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 4630,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'NONE',  'ON': [4630], 'OFF': [320,7160,9999,91,777,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4NET LARES RPT',    'TS': 1, 'TGID': 4630,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4630], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 4630,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4630], 'OFF': [320,7160,9999,91,777,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 4630,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4630], 'OFF': [320,7160,9999,91,777,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'DMR+ REF4630 PR',    'TS': 2, 'TGID': 9,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'XLX-215A',    'TS': 2, 'TGID': 9,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 4630,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []}, 
        ],
    'TG777 Boriken': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 777,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [777], 'OFF': [320,7160,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 777,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [777], 'OFF': [320,7160,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 777,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [777], 'OFF': [320,7160,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 777,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [777], 'OFF': [320,7160,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 777,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [777], 'OFF': [320,7160,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4NET LARES RPT',    'TS': 2, 'TGID': 777,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [777], 'OFF': [320,7160,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4AP-OBP',    'TS': 1, 'TGID': 777, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'EA1HNC-OBP',    'TS': 1, 'TGID': 777, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'N2USB-OBP',    'TS': 1, 'TGID': 777, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'LU8ANB-OBP',    'TS': 1, 'TGID': 777, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 777,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'HB-Peru',    'TS': 1, 'TGID': 777,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},        
        ],
    'HB Peru': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 7160,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [7160], 'OFF': [320,777,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 7160,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [7160], 'OFF': [320,777,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 7160,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [7160], 'OFF': [320,777,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 7160,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [7160], 'OFF': [320,777,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 7160,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [7160], 'OFF': [320,777,9999,91,4630,77,33015,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 7160,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'HB-Peru',    'TS': 1, 'TGID': 7160,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},        
        ],
    'AMSAT': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 98006,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [98006], 'OFF': [320,7160,9999,91,4630,777,77,33015,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 98006,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [98006], 'OFF': [320,7160,9999,91,4630,777,77,33015,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 98006,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [98006], 'OFF': [320,7160,9999,91,4630,777,77,33015,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 98006,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [98006], 'OFF': [320,7160,9999,91,4630,777,77,33015,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 98006,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [98006], 'OFF': [320,7160,9999,91,4630,777,77,33015,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'BM3103-OBP',    'TS': 1, 'TGID': 98006, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 98006,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'TG3199': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 3199,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [3199], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 3199,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [3199], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 3199,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [3199], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 3199,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [3199], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 3199,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [3199], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'BM3103-OBP',    'TS': 1, 'TGID': 3199, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 3199,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'TG7225': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 7225,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [7225], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 7225,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [7225], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 7225,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [7225], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 7225,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [7225], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 7225,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [7225], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'BM3103-OBP',    'TS': 1, 'TGID': 7225, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 7225,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'TG7227': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 7227,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [7227], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 7227,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [7227], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 7227,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [7227], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,37030,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 7227,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [7227], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 7227,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [7227], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,37030,31012], 'RESET': []},
            {'SYSTEM': 'BM3103-OBP',    'TS': 1, 'TGID': 7227, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 7227,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'TG37030': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 37030,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [37030], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 37030,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [37030], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 37030,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [37030], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 37030,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [37030], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 37030,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [37030], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,31012], 'RESET': []},
            {'SYSTEM': 'BM3103-OBP',    'TS': 1, 'TGID': 37030, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 37030,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'TG31012': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 31012,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [31012], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 31012,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [31012], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 31012,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [31012], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 31012,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [31012], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 31012,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [31012], 'OFF': [320,7160,9999,91,4630,777,77,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'BM3103-OBP',    'TS': 1, 'TGID': 31012, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 31012,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'ON Demand': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 91,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [91], 'OFF': [320,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 91,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [91], 'OFF': [320,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 91,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [91], 'OFF': [320,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 91,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [91], 'OFF': [320,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 91,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [91], 'OFF': [320,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'ON-DEMAND',    'TS': 2, 'TGID': 91, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 91,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'PARROT': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 9999,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [9999], 'OFF': [320,7160,91,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 9999,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [9999], 'OFF': [320,7160,91,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4NET LARES RPT',    'TS': 2, 'TGID': 9999,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [9999], 'OFF': [320,7160,91,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 9999,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [9999], 'OFF': [320,7160,91,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 9999,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [9999], 'OFF': [320,7160,91,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 9999,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [9999], 'OFF': [320,7160,91,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'PARROT',    'TS': 2, 'TGID': 9999, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
    'Private': [
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 320,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [320], 'OFF': [91,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 320,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [320], 'OFF': [91,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 320,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [320], 'OFF': [91,7160,9999,77,4630,777,31012,33015,98006,3199,7225,7227,37030], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 320,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
     'TG33015 DMRplus': [
            {'SYSTEM': 'KP4ECO AGUADA RPT',    'TS': 2, 'TGID': 33015,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [33015], 'OFF': [320,7160,9999,91,4630,777,77,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4ECO MOCA RPT',    'TS': 2, 'TGID': 33015,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [33015], 'OFF': [320,7160,9999,91,4630,777,77,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HIGH POWER HOTSPOT ANASCO',    'TS': 2, 'TGID': 33015,    'ACTIVE': False, 'TIMEOUT': 5, 'TO_TYPE': 'ON',  'ON': [33015], 'OFF': [320,7160,9999,91,4630,777,77,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'WP3JJ HOTSPOTS',    'TS': 2, 'TGID': 33015,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [33015], 'OFF': [320,7160,9999,91,4630,777,77,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'KP4CA HOTSPOTS',    'TS': 2, 'TGID': 33015,    'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [33015], 'OFF': [320,7160,9999,91,4630,777,77,98006,3199,7225,7227,37030,31012], 'RESET': []},
            {'SYSTEM': 'DMR+ TG33015',    'TS': 2, 'TGID': 33015, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'TGIF TG33015',    'TS': 2, 'TGID': 33015, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'AREDN KP4CA HBLINK',    'TS': 1, 'TGID': 33015,    'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ]
}

if __name__ == '__main__':
    from pprint import pprint
    pprint(BRIDGES)
