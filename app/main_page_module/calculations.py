import math

def calclulate_food(peoplenum, vegiSlider, childnum, vegiChild, cevap, plesk, vratovina, perutinicke,
                    bucke, gobce, paprikas, melancanno, pivicko, colica, sokec, ledek):

    #izracun ljudi in otrok mesojedcev
    mesojedci = peoplenum - vegiSlider
    otroci_mesa = childnum - vegiChild  
    #skupno vsi ljudje
    skupno_ljudje = peoplenum + childnum
    
    #meso
    skupna_mozna_kolicina_mesa = cevap + plesk + vratovina + perutinicke
    #        
    cevap_proc = cevap * 1 / skupna_mozna_kolicina_mesa
    plesk_proc = plesk * 1 / skupna_mozna_kolicina_mesa
    vratovina_proc = vratovina * 1 / skupna_mozna_kolicina_mesa
    perutinicke_proc = perutinicke * 1 / skupna_mozna_kolicina_mesa   
    
    #zelenjava
    skupna_mozna_kolicina_zelenjave = bucke + gobce + paprikas + melancanno
    #           
    bucke_proc = bucke * 1 / skupna_mozna_kolicina_zelenjave
    gobce_proc = gobce * 1 / skupna_mozna_kolicina_zelenjave
    paprikas_proc = paprikas * 1 / skupna_mozna_kolicina_zelenjave
    melancanno_proc = melancanno * 1 / skupna_mozna_kolicina_zelenjave
    
    #pijaca
    skupna_mozna_kolicina_brezalko = colica + sokec
    colica_proc = colica / skupna_mozna_kolicina_brezalko
    sokec_proc = sokec / skupna_mozna_kolicina_brezalko
    #
    ledek_proc = ledek * 1 / 50
    
    #
    
    meso_odrasli_g = 200
    meso_otroci_g = 100
    
    vegi_odrasli_g = 200
    vegi_otroci_g = 100
    
    zelenjava_odrasli_g = 200
    zelenjava_otroci_g = 100
    
    perutnicke_razmerje = 1.6
    
    kruh_odrasli_g = 100
    kruh_otroci_g = 50
    
    cebula_odrasli_g = 25
    cebula_otroci_g = 15
    
    pivo_ml = pivicko * 500
    cola_odrasli_ml = 1200
    cola_otroci_ml = 700
    sok_odrasli_ml = 780
    sok_otroci_ml = 455
    led_odrasli_g = 750
    
    #teza na kos
    kruh_g = 50
        
    
    #results
    
    #meso
    skupno_cevap = int(((mesojedci * meso_odrasli_g) + (otroci_mesa * meso_otroci_g)) * cevap_proc)
    skupno_plesk = int(((mesojedci * meso_odrasli_g) + (otroci_mesa * meso_otroci_g)) * plesk_proc)
    skupno_vratovina = int(((mesojedci * meso_odrasli_g) + (otroci_mesa * meso_otroci_g)) * vratovina_proc)
    skupno_perutinicke = int(((mesojedci * meso_odrasli_g) + (otroci_mesa * meso_otroci_g)) * perutnicke_razmerje * perutinicke_proc)

    skupna_meso = skupno_cevap + skupno_plesk + skupno_vratovina + skupno_perutinicke
    
    #vegi
    skupno_vegi = ((vegiSlider * meso_odrasli_g) + (vegiChild * meso_otroci_g))
    #zelenjava
    skupno_bucke = int(((peoplenum * zelenjava_odrasli_g) + (childnum * zelenjava_otroci_g)) * bucke_proc)
    skupno_gobce = int(((peoplenum * zelenjava_odrasli_g) + (childnum * zelenjava_otroci_g)) * gobce_proc)
    skupno_paprikas = int(((peoplenum * zelenjava_odrasli_g) + (childnum * zelenjava_otroci_g)) * paprikas_proc)
    skupno_melancanno = int(((peoplenum * zelenjava_odrasli_g) + (childnum * zelenjava_otroci_g)) * melancanno_proc)
    #pivo
    skupno_pivo = peoplenum * pivo_ml
    skupno_pivo_veliko = int(skupno_pivo / 500) + (skupno_pivo % 500 > 0)
    skupno_pivo_malo = int(skupno_pivo / 330) + (skupno_pivo % 330 > 0)
    #brezalko
    skupno_cola = ((peoplenum * cola_odrasli_ml) + (childnum * cola_otroci_ml)) * colica_proc
    skupno_cola_literpol = int(skupno_cola / 1500) + (skupno_cola % 1500 > 0)        
    skupno_sok = ((peoplenum * sok_odrasli_ml) + (childnum * sok_otroci_ml)) * sokec_proc
    skupno_sok_liter = int(skupno_sok / 1000) + (skupno_sok % 1000 > 0)
    #led
    skupno_led_g = skupno_ljudje * led_odrasli_g * ledek_proc
    #ostalo
    skupno_cebula_g = (peoplenum * cebula_odrasli_g) + (childnum * cebula_otroci_g)
    skupno_kruh_g = (peoplenum * kruh_odrasli_g) + (childnum * kruh_otroci_g)
    skupno_kruh_kos = int(skupno_kruh_g / kruh_g) + (skupno_kruh_g % kruh_g > 0)    
    skupno_oglje = skupna_meso + skupno_vegi
    
    namazi = math.ceil((skupno_ljudje / 8)) * 0.25
    
    osnovni_p = {"odrasli_m": ["Število odraslih - Meso", mesojedci],
     "odrasli_v": ["Število odraslih - Vegi", vegiSlider],
     "otroci_m": ["Število otrok - Meso", otroci_mesa],
     "otroci_v": ["Število otrok - Vegi", vegiChild]
     }
    
    meso = {"cevap": ["Čevapčiči", round(skupno_cevap * 0.001, 2)],
     "plesk": ["Pleskavice", round(skupno_plesk * 0.001, 2)],
     "vrat": ["Vratovina", round(skupno_vratovina * 0.001, 2)],
     "perut": ["Perutničke", round(skupno_perutinicke * 0.001, 2)]
     }
    
    vegi = {
     "vegi": ["Vegi odrasli", skupno_vegi]
     }
    
    zelenjava = {"bucke": ["Bučke", round(skupno_bucke * 0.001, 2)],
     "gobe": ["Gobice", round(skupno_gobce * 0.001, 2)],
     "pap": ["Paprika", round(skupno_paprikas * 0.001, 2)],
     "melan": ["Melancani", round(skupno_melancanno * 0.001, 2)]
     }
    
    pivo = {"skup_pivo": ["Skupno Pivo ml", round(skupno_pivo * 0.001, 2)],
     "veliko_pivo": ["Velikega", skupno_pivo_veliko],
     "malo_pivo": ["Ali majhnega", skupno_pivo_malo]
     }
    
    sokovi = {"skup_cola": ["Skupno Cola ml", round(skupno_cola * 0.001, 2)],
     "cola_literpol": ["Cola 1,5l", skupno_cola_literpol],
     "skup_sok": ["Skupno Sok", round(skupno_sok * 0.001, 2)],
     "sok_liter": ["Sokl 1l", skupno_sok_liter]
     }
    
    ostalo = {"led_g": ["Gramov Ledu", round(skupno_led_g * 0.001, 2)],
     "gram_veb": ["Gramov čebule", round(skupno_cebula_g * 0.001, 2)],
     "gram_kruh": ["Gramov kruha", round(skupno_kruh_g * 0.001, 2)],
     "kos_kruh": ["Kosov kruha", skupno_kruh_kos],
     "kajmak": ["Kajmak", namazi],
     "ajvar": ["Ajvar", namazi],
     "ketchup": ["Ketchup", namazi],
     "majoneza": ["Majoneza", round(namazi /2, 2)],
     "pikantna": ["Robit Hot", 1],
     "skupno_oglje": ["Oglje", round(skupno_oglje * 0.001, 2)],
     "olje": ["Olje", 1],     
     "rola_papir": ["Rola papirja", 1],
     "servjet": ["Servjeti", skupno_ljudje * 4],
     "vrece_cmeti": ["Vreče za smeti", math.ceil(skupno_ljudje * 0.2)],
     "kozarci": ["Kozarci", skupno_ljudje * 3],
     "krozniki": ["Krožniki", skupno_ljudje * 2]
    }
    
    return osnovni_p, meso, vegi, zelenjava, pivo, sokovi, ostalo