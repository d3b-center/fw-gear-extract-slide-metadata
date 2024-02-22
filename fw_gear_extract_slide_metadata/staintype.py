import re
def staintype(fname):
 if re.search('.*AE1_AE3.*', fname) or re.search('.*AE1-AE3.*', fname):
    return("AE1_AE3")
 elif re.search('.*ACTH.*', fname):
    return("ACTH")
 elif re.search('.*AE1.*', fname):
    return('AE1')
 elif re.search('.*AFB.*', fname):
    return('AFB')
 elif re.search('.*AFP.*', fname):
    return('AFP')
 elif re.search('.*Alcian_blue.*', fname):
    return('Alcian_blue')
 elif re.search('.*ALK.*', fname):
    return('ALK')
 elif re.search('.*ATRX.*', fname):
    return('ATRX')
 elif re.search('.*ATTR.*', fname):
    return('ATTR')
 elif re.search('.*B-Catenin.*', fname) or re.search('.*BCATENIN.*', fname) or re.search('.*Beta_cat.*',fname) or re.search('.*Beta_catenin.*', fname) or re.search('.*Beta-catinin.*', fname):
    return('B-Catenin')
 elif re.search('.*BCoR.*', fname):
    return('BCoR')
 elif re.search('.*Brach.*', fname) or re.search('.*Brachyury.*', fname) or re.search('.*BRACHYURY_CTRL.*',  fname) or re.search('.*BRACKYURY.*', fname):
    return('Brachyury')
 elif re.search('.*BRG-1.*', fname) or re.search('.*BRG1.*', fname):
    return('BRG1')
 elif re.search('.*C-kit.*', fname):
    return('C-kit')
 elif re.search('.*CAM.*', fname):
    return('CAM 5.2')
 elif re.search('.*CD1[^0-9]', fname):
    return('CD1')
 elif re.search('.*CD10[^0-9]', fname):
    return('CD10')
 elif re.search('.*CD117[^0-9]', fname):
    return('CD117')
 elif re.search('.*CD163[^0-9]', fname):
    return('CD163')
 elif re.search('.*CD19[^0-9]', fname):
    return('CD19')
 elif re.search('.*CD20[^0-9]', fname):
    return('CD20')
 elif re.search('.*CD3[^0-9]', fname):
    return('CD3')
 elif re.search('.*CD30[^0-9]', fname):
    return('CD30')
 elif re.search('.*CD31[^0-9]', fname):
    return('CD31')
 elif re.search('.*CD33[^0-9]', fname):
    return('CD33')
 elif re.search('.*CD34[^0-9]', fname):
    return('CD34')
 elif re.search('.*CD4[^0-9]', fname):
    return('CD4')
 elif re.search('.*CD42[^0-9]', fname):
    return('CD42')
 elif re.search('.*CD30[^0-9]', fname):
    return('CD30')
 elif re.search('.*CD45[^0-9]', fname) or re.search('.*CD-45[^0-9]', fname):
    return('CD45')
 elif re.search('.*CD5[^0-9]', fname):
    return('CD5')
 elif re.search('.*CD56[^0-9]', fname):
    return('CD56')
 elif re.search('.*CD57[^0-9]', fname) or re.search('.*CD-57[^0-9]', fname):
    return('CD57')
 elif re.search('.*CD68[^0-9]', fname):
    return('CD68')
 elif re.search('.*CD79[^0-9]', fname):
    return('CD79')
 elif re.search('.*CD8[^0-9]', fname):
    return('CD8')
 elif re.search('.*CD99[^0-9]', fname):
    return('CD99')
 elif re.search('.*CFAP.*', fname):
    return('CFAP')
 elif re.search('.*Chrom.*', fname) or re.search('.*CHROMO.*', fname) or re.search('.*Chromograni.*', fname) or re.search('.*Chromogranin.*', fname) or re.search('.*Cromogranin.*', fname):
    return('Chromogranin')
 elif re.search('.*CYTOKERATIN.*', fname):
    return('CK')
 elif re.search('.*CK20.*', fname):
    return('CK20')
 elif re.search('.*CK_7.*', fname) or re.search('.*CK7.*', fname):
    return('CK7')
 elif re.search('.*cytology.*', fname):
    return('cytology')
 elif re.search('.*DES.*', fname) or re.search('.*Desmin.*', fname):
    return('Desmin')
 elif re.search('.*ECAD.*', fname) or re.search('.*ECAD_CTRL.*', fname):
    return('ECAD')
 elif re.search('.*EGFR.*', fname):
    return('EGFR')
 elif re.search('.*ELASTIC.*', fname):
    return('ELASTIC')
 elif re.search('.*EMA.*', fname):
    return('EMA')
 elif re.search('.*EZHIP.*', fname):
    return('EZHIP')
 elif re.search('.*F_VIII.*', fname) or re.search('.*F8.*', fname):
    return('Factor VIII')
 elif re.search('.*Factor_XIII.*', fname):
    return('Factor XIII')
 elif re.search('.*Filamin.*', fname) or re.search('.*Fimamin.*', fname):
    return('Filamin')
 elif re.search('.*FITES.*', fname):
    return(f"Fite's")
 elif re.search('.*Fontana.*', fname):
    return('Fontana')
 elif re.search('.*FS.*', fname):
    return('FS')
 elif re.search('.*FSB.*', fname):
    return('FSB')
 elif re.search('.*FSH.*', fname):
    return('FSH')
 elif re.search('.*GAB.*', fname) or re.search('.*GAB1.*', fname):
    return('GAB-1')
 elif re.search('.*GATA3.*', fname):
    return('GATA3')
 elif re.search('.*GFAP.*', fname):
    return('GFAP')
 elif re.search('.*GH.*', fname):
    return('GH')
 elif re.search('.*GLUT-1.*', fname):
    return('GLUT-1')
 elif re.search('.*Glypican.*', fname):
    return('Glypican')
 elif re.search('.*GMS.*', fname):
    return('GMS')
 elif re.search('.*GRAM.*', fname):
    return('GRAM')
 elif re.search('.*HandE.*', fname) or re.search('.*H&E.*', fname) or re.search('.*HEE.*', fname) or re.search('.*HHE.*',fname) or re.search('.*H_and_E.*', fname) or re.search('.*HE.*', fname):
    return('HandE')
 elif re.search('.*H3K27me3.*', fname):
    return('H3K27me3')
 elif re.search('.*HCG.*', fname):
    return('HCG')
 elif re.search('.*Her2_Neu.*', fname):
    return('Her2_Neu')
 elif re.search('.*Histone.*', fname):
    return('Histone')
 elif re.search('.*Histone3.*', fname):
    return('Histone3')
 elif re.search('.*HMB45.*', fname):
    return('HMB45')
 elif re.search('.*HMWK.*', fname):
    return('HMWK')
 elif re.search('.*iba1.*', fname):
    return('iba1')
 elif re.search('.*IDH-1.*', fname) or re.search('.*IDH1.*', fname):
    return('IDH1')
 elif re.search('.*Inhibin.*', fname):
    return('Inhibin')
 elif re.search('.*INI.*', fname):
    return('INI1')
 elif re.search('.*Iron.*', fname):
    return('Iron')
 elif re.search('.*Ki-67.*', fname):
    return('Ki-67')
 elif re.search('.*Klover.*', fname) or re.search('.*Kluver.*', fname):
    return('Kluver')
 elif re.search('.*Langerin.*', fname) or re.search('.*Langherin.*', fname):
    return('Langerin')
 elif re.search('.*LEF.*', fname):
    return('LEF-1')
 elif re.search('.*LFB.*', fname) or re.search('.*Luxol.*', fname) or re.search('.*Luxol_Fast_blue.*', fname):
    return('LFB')
 elif re.search('.*LH.*', fname):
    return('LH')
 elif re.search('.*LMWK.*', fname):
    return('LMWK')
 elif re.search('.*M-TRI.*', fname):
    return('M-TRI')
 elif re.search('.*MAP2.*', fname):
    return('MAP2')
 elif re.search('.*MIC.*', fname):
    return('MIC2')
 elif re.search('.*MYOD1.*', fname):
    return('MYOD1')
 elif re.search('.*MYOG.*', fname) or re.search('.*MyOGENIN.*', fname):
    return('MYOG')
 elif re.search('.*NB84.*', fname):
    return('NB84')
 elif re.search('.*NEU-N.*', fname) or re.search('.*NEUN.*', fname):
    return('NEUN')
 elif re.search('.*NF2[^A-Z]', fname):
    return('NF2')
 elif re.search('.*NF_2F11.*', fname) or re.search('.*NF2F11.*', fname) or re.search('.*NF2FII.*', fname) or re.search('.*NF2N11.*', fname):
    return('NF2F11')
 elif re.search('.*Neurofilament.*', fname) or re.search('.*NF.*', fname) or re.search('.*NFP.*', fname):
    return('NFP')
 elif re.search('.*NKX2.2.*', fname):
    return('NKX2.2')
 elif re.search('.*NSE.*', fname):
    return('NSE')
 elif re.search('.*O13.*', fname):
    return('O13')
 elif re.search('.*Octa-4.*', fname) or re.search('.*OCTA4.*', fname):
    return('Octa-4')
 elif re.search('.*Olig.*', fname):
    return('OLIG')
 elif re.search('.*OLIG2.*', fname):
    return('OLIG2')
 elif re.search('.*ORO.*', fname):
    return('ORO')
 elif re.search('.*P52.*', fname):
    return('P52')
 elif re.search('.*P53.*', fname):
    return('P53')
 elif re.search('.*Pan_Keratin.*', fname):
    return('Pan-Keratin')
 elif re.search('.*PAS.*', fname):
    return('PAS')
 elif re.search('.*PAS-D.*', fname):
    return('PAS-D')
 elif re.search('.*PGP.*', fname):
    return('PGP')
 elif re.search('.*PHH3.*', fname):
    return('PHH3')
 elif re.search('.*PHOX2B.*', fname):
    return('PHOX2B')
 elif re.search('.*PLAP.*', fname):
    return('PLAP')
 elif re.search('.*PRL.*', fname) or re.search('.*Prolactin.*', fname):
    return('PRL')
 elif re.search('.*RA21.*', fname):
    return('RA21')
 elif re.search('.*RET.*', fname):
    return('RET')
 elif re.search('.*RETIC.*', fname) or re.search('.*Reticulin.*', fname):
    return('Reticulin')
 elif re.search('.*S100.*', fname):
    return('S100')
 elif re.search('.*SALL4.*', fname):
    return('SALL4')
 elif re.search('.*SATB2.*', fname):
    return('SATB2')
 elif re.search('.*SF1.*', fname):
    return('SF1')
 elif re.search('.*SMA.*', fname):
    return('SMA')
 elif re.search('.*SOX.*', fname):
    return('SOX10')
 elif re.search('.*SSTR2.*', fname):
    return('SSTR2')
 elif re.search('.*STAT_6.*', fname):
    return('STAT6')
 elif re.search('.*SV40.*', fname):
    return('SV40')
 elif re.search('.*SYN.*', fname) or re.search('.*Synapto.*', fname) or re.search('.*Synaptophysin.*', fname):
    return('Synaptophysin')
 elif re.search('.*T14.*', fname):
    return('T14')
 elif re.search('.*TDT.*', fname):
    return('TDT')
 elif re.search('.*TH.*', fname):
    return('TH')
 elif re.search('.*Tol_blue.*', fname):
    return('Toluidine blue')
 elif re.search('.*TOXO.*', fname):
    return('TOXO')
 elif re.search('.*TP1.*', fname):
    return('TP1')
 elif re.search('.*TRICHROME.*', fname):
    return('TRICHROME')
 elif re.search('.*Trimethyl.*', fname):
    return('Trimethyl')
 elif re.search('.*TSH.*', fname):
    return('TSH')
 elif re.search('.*TTR.*', fname):
    return('TTR')
 elif re.search('.*VIM.*', fname) or re.search('.*Vimentin.*', fname):
    return('Vimentin')
 elif re.search('.*WT1.*', fname):
    return('WT1')
 elif re.search('.*YAP.*', fname):
    return('YAP')
 else:
    return('No-stain-type')