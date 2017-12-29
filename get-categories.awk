#! /bin/awk

BEGIN { FPAT='([^,]+)|("[^"]+")' }
{ print $8 }
