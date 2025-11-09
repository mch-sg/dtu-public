#
# OBS: Indså nogle fejl ved den første version, namely, at jeg fik minutter som 60 og timer som alt muligt, da jeg ikke havde antal timer der skal sættes frem, men kun en time. 
# Derudover ellers nogle små rettelser, bør gerne virke bedre nu. Tjek gerne løs og ser frem til jeres feedback hvis der er andre mangler :)
#
def arrival_times(schedule, delay):
    nstr = []
    arr = []

    for j in range(len(schedule)):  #  Split dit schedule array op i tal timer og minutter for hver
        nstr += schedule[j].split(":")

    for i in range(len(schedule)):  #  Loop igennem længden af skemaet
        hh = int(nstr[2*i])  #  Sæt timer som værende alle de lige tal i mit array 'nstr' (2k)
        mm = int(nstr[2*i+1])  #  Sæt minutter som værende alle ulige tal i mit array 'nstr' (2k+1)
        mm_delay = mm + delay  #  Antal minutter forsinket

        ntimes = mm_delay // 60  #  Hvor mange gange antal minutter forsinket går op i 60, i.e. hvor mange timer der skal sættes frem
        hh += ntimes  #  Antal timer der sættes frem 
        mm_delay = mm_delay % 60  #  Resten af minutterne når de er forsinket skal være minutterne
        
        hh = hh % 24

        arr.append(f"{hh:02}:{mm_delay:02}")

    return arr

h = arrival_times(['12:37', '08:10', '23:59'], 25)
print(h)
b = arrival_times(['12:37', '08:10', '23:59'], 50)
print(b)
v = arrival_times(['12:37', '08:10', '23:59'], 123)
print(v)