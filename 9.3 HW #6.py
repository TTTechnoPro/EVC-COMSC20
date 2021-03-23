#!/usr/bin/env python3

#Question 1
'''
‘Python’[1] = 'y'
“Strings are sequences of characters.”[5] = 'g'
len(“wonderful”) = 9
‘Mystery’[:4] = Myst
‘p’ in ‘Pineapple’ = True
‘apple’ in ‘Pineapple’ = True
‘pear’ not in ‘Pineapple’ = True
‘apple’ > ‘pineapple’ = False
‘pineapple’ < ‘Peach’ = False
'''

#Question 2
prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p +"u"+ suffix)
    else:
        print(p+suffix)

#Question 3
longString = '''heyheyheyyyyyy heyheyHEYYYyyyy heyheyheyyyyy wasasasasasasassasupppp BITCONNECTTTTTTTTT HEYHEYHEY everybody my name is CARLOS MARDOS and I am coming from NEW YORK CITY , NewYork. LEMME tell you guys that I am SO ExCited I amSO HAppy I am really SO ThRILLED to be right NOW SHaRING thiS AMAZING GLORIOUS SuPER and eXcITiNG mOMent oF myLIfe wiTH alL of yOU GUYs. anD lEmmE tell U that we ARe REally ChanGing thE wOrLD aS wE kNow It. ThE WOrld is NOt AnY mOre, tHE wAy it USed tO bE MMM MMMM MMM NO NO NO BIIIIITTTCONNNNNECTTTTTTT WWOWW BIIIIITCONENNNEEEEEECCCCCCCCTTTTTT WE arE cOMING and wE aRE cOMinG iN WAVES wE arE StaRTing aND We ARe gOING to WaTcH iT Go ALL OVER THE WORLD! wE ARE [unintelligible] the ENtIRE wORLd! LEMME telL u GUYs tHAt I StArted onehundredthirtyseven days ago with only TwEnTY FiVE ThouSAND sIX HunDred TeN DolLAR$ anD rIGht nOW I aM reACHing One HUnDred FouRTY THouSAND DoLLaRSSS! WOAHWOAHWOAHWOAHWOAHWOAH WASSUPPP! aND LeMME TeLL YoU tHaT I aM aCtUally EarNING aROuND One HunDre— I MeaN oNe ThoUSANd anD FouR HunDreD DollArs oN aN eVErYdAy BaSiS SeVen DayS a WeeK WHATTTTTTTTT!!!! IAm RigHT nOw InDependeNTly fInaNciALly iNDepEndenTly. IAM SaYinG tO So MaNy PeoPLe wHo SaId tHaT thIS WAS goIng to bE a Con-ArTisT gaMe, tHaT tHis wAs GoiNg to Be a ScAMMER gAme! "HeY! You'Re GoNNa LoSE All YoUR MonEY" MY WIFE StILl DoesN't BeliEVe in ME! i'M tELLing hIm WeLL HONEY LiSTE— THIS is ReALLLL "nONOnONO tHAT's A SCAm!" anD I saID bUT waIT ImA go To thE BANk ImA get My BItCOiNS Im GoinG tO AcTuallY pUt iT iNTO DollAR$ HERE THEY'RE RIgHT oN thE tAbLE "NAWW THAt's MoNeY tHaT yOU ToOk fRoM aNothEr AccOunT" I saY WHAT'M I GuNNA DOOO? NoW iSAiD tO My mYseLF "yOu Know What", wHeN I AM sTarTinG to pUt TeN THoUSAND tHoUSAnD dAILY HUH RiGhT oN hER you kNOw oN hEr TaBle, tHeN sHe'S GonnA SAY "WOAHHHHH HAHAHAHAHA YUHUHUYHUHUHHUHUH  OkAY ThAT'S rEAL!" sO gUYs iWaNNa TeLl YoU SomETHing. STAy anD BeLIevE iS tHe OnE ThInG wE AlL neED tO bE AbLe to ChaNGE tHe WorLD
wE AlL neED tO bE AbLe to ChaNGE tHe WorLD anD RiGhT nOW i BeLIEvE tHaT iN thIs RoOM, wE hAVe THe SEEd thAt'S GerMinATe anD tHAt'S GoiNg tO ExPLODe intO an AMMMMAZING oPpOrTuNItY fOR US tO ChAnGE tHIS eNTiRE WOrLD. I Am So PrOUD I Am So HonOREd I aM sO ExCited To bE HeRE RigHT NOw anD LemME teLl YoU sOmeThing ThAt eACh aNd EvERy onE of YoU hAs thE OppOrtUNity to bECOMe LiKE tHoSe AmaZING PeOPLe tHAt wE KnOW Here fROM ViETnaM! HEYY HEYY mY [unintelligible] fRoM vIEtNAm MaKInG SO MUcH mONEY ThAt ThEy CaN ProBaBly hAvE A rEaL HaRD TiME CoUNtINg iTTTT! HAHAHAHA so gUYs! LeMMe TeLL You! i LLLLLLLLLLLOOOOOOOOOOOOOOOVVVVVVVVVEEEEEEEEEEEEEEEEEE  BIIIIIIIIIIITTTTTCONNNNNNNNECCCCCCCCCCTTTT (finally returns the mic)
'''

def alphaCharacters (string):
    totalE = 0;
    totalChar = 0;
    for i in string:
        if i == "e":
            totalE+=1
        if i.isalnum():
            totalChar+=1
    print("Your text contains", str(totalChar), "alphabetic characters, of which", str(totalE), "or", str(round(totalE/totalChar,2))+"%" ,"are 'e'.")

alphaCharacters(longString)

#Question 8
def remove(string):
    testString = "The quick brown fox jumps over the lazy dog"
    return testString.replace(string,"")

print(remove("e"))

#Question 10
def CountOccurrences(string, substring):
    count = 0
    start = 0

    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count
print(CountOccurrences("MegaChad6969696969969fromLTT6969696969", "69"))

#Question 18
def EncryptMessage (string, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newString = ""
    for i in string:
        if i == ' ':
            newString += ' '
        else:
            newString += cipher[alphabet.index(i)]
    return newString
print(EncryptMessage("hello world", "badcfehgjilknmporqtsvuxwzy"))


