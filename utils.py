import pandas as pd
import numpy as np


def read_atlas_csv(path):
    data = pd.read_csv(path, delimiter='\s+', header=None)



    data_o = data[data[5]=='o']
    data_c = data[data[5]=='c']
    data_o = data_o.reset_index(drop=True)
    data_c = data_c.reset_index(drop=True)


    data_c['t'] = pd.to_numeric(data_c[0], errors='coerce')
    data_c['m'] = pd.to_numeric(data_c[1], errors='coerce')
    data_c['m_err'] = pd.to_numeric(data_c[2], errors='coerce')
    data_c['f'] = pd.to_numeric(data_c[3], errors='coerce')
    data_c['f_err'] = pd.to_numeric(data_c[4], errors='coerce')
    data_c['filter'] = pd.to_numeric(data_c[5], errors='coerce')
    data_c['tphot_err'] = pd.to_numeric(data_c[6], errors='coerce')
    data_c['chi/N'] = pd.to_numeric(data_c[7], errors='coerce')
    data_c['RA'] = pd.to_numeric(data_c[8], errors='coerce')
    data_c['Dec'] = pd.to_numeric(data_c[9], errors='coerce')
    data_c['x']= pd.to_numeric(data_c[10], errors='coerce')
    data_c['y'] = pd.to_numeric(data_c[11], errors='coerce')
    data_c['maj'] = pd.to_numeric(data_c[12], errors='coerce')
    data_c['min'] = pd.to_numeric(data_c[13], errors='coerce')
    data_c['phi'] = pd.to_numeric(data_c[14], errors='coerce')
    data_c['apfit'] = pd.to_numeric(data_c[15], errors='coerce')
    data_c['mag5sigma'] = pd.to_numeric(data_c[16], errors='coerce')
    data_c['sky'] = pd.to_numeric(data_c[17], errors='coerce')
    data_c['obs'] = pd.to_numeric(data_c[18], errors='coerce')



    data_o['t'] = pd.to_numeric(data_o[0], errors='coerce')
    data_o['m'] = pd.to_numeric(data_o[1], errors='coerce')
    data_o['m_err'] = pd.to_numeric(data_o[2], errors='coerce')
    data_o['f'] = pd.to_numeric(data_o[3], errors='coerce')
    data_o['f_err'] = pd.to_numeric(data_o[4], errors='coerce')
    data_o['filter'] = pd.to_numeric(data_o[5], errors='coerce')
    data_o['tphot_err'] = pd.to_numeric(data_o[6], errors='coerce')
    data_o ['chi/N']= pd.to_numeric(data_o[7], errors='coerce')
    data_o['RA'] = pd.to_numeric(data_o[8], errors='coerce')
    data_o['Dec'] = pd.to_numeric(data_o[9], errors='coerce')
    data_o['x'] = pd.to_numeric(data_o[10], errors='coerce')
    data_o['y'] = pd.to_numeric(data_o[11], errors='coerce')
    data_o['maj'] = pd.to_numeric(data_o[12], errors='coerce')
    data_o['min'] = pd.to_numeric(data_o[13], errors='coerce')
    data_o['phi'] = pd.to_numeric(data_o[14], errors='coerce')
    data_o['apfit'] = pd.to_numeric(data_o[15], errors='coerce')
    data_o['mag5sigma'] = pd.to_numeric(data_o[16], errors='coerce')
    data_o['sky'] = pd.to_numeric(data_o[17], errors='coerce')
    data_o['obs'] = pd.to_numeric(data_o[18], errors='coerce')




    data_c.drop(columns=[0], inplace=True)
    data_c.drop(columns=[1], inplace=True)
    data_c.drop(columns=[2], inplace=True)
    data_c.drop(columns=[3], inplace=True)
    data_c.drop(columns=[4], inplace=True)
    data_c.drop(columns=[5], inplace=True)
    data_c.drop(columns=[6], inplace=True)
    data_c.drop(columns=[7], inplace=True)
    data_c.drop(columns=[8], inplace=True)
    data_c.drop(columns=[9], inplace=True)
    data_c.drop(columns=[10], inplace=True)
    data_c.drop(columns=[11], inplace=True)
    data_c.drop(columns=[12], inplace=True)
    data_c.drop(columns=[13], inplace=True)
    data_c.drop(columns=[14], inplace=True)
    data_c.drop(columns=[15], inplace=True)
    data_c.drop(columns=[16], inplace=True)
    data_c.drop(columns=[17], inplace=True)
    data_c.drop(columns=[18], inplace=True)


    data_o.drop(columns=[0], inplace=True)
    data_o.drop(columns=[1], inplace=True)
    data_o.drop(columns=[2], inplace=True)
    data_o.drop(columns=[3], inplace=True)
    data_o.drop(columns=[4], inplace=True)
    data_o.drop(columns=[5], inplace=True)
    data_o.drop(columns=[6], inplace=True)
    data_o.drop(columns=[7], inplace=True)
    data_o.drop(columns=[8], inplace=True)
    data_o.drop(columns=[9], inplace=True)
    data_o.drop(columns=[10], inplace=True)
    data_o.drop(columns=[11], inplace=True)
    data_o.drop(columns=[12], inplace=True)
    data_o.drop(columns=[13], inplace=True)
    data_o.drop(columns=[14], inplace=True)
    data_o.drop(columns=[15], inplace=True)
    data_o.drop(columns=[16], inplace=True)
    data_o.drop(columns=[17], inplace=True)
    data_o.drop(columns=[18], inplace=True)



    data_o.drop(columns=['filter'], inplace=True)
    data_c.drop(columns=['filter'], inplace=True)





    data_o= data_o.reset_index(drop=True)
    data_c= data_c.reset_index(drop=True)


    data_o = data_o[data_o['f']>0]
    data_c = data_c[data_c['f']>0]

    data_o= data_o.reset_index(drop=True)
    data_c= data_c.reset_index(drop=True)



    data_o['err/f *100']= data_o['f_err']/ data_o['f']*100
    data_c['err/f *100']= data_c['f_err']/ data_c['f']*100


    data_o['chi/N'] = data_o['chi/N'][data_o['chi/N'] > 0]
    data_c['chi/N'] = data_c['chi/N'][data_c['chi/N'] > 0]

    data_o['log_redchi'] = np.log10(data_o['chi/N'])
    data_c['log_redchi'] = np.log10(data_c['chi/N'])




    data_o['err/f *100'] = data_o['err/f *100'][data_o['err/f *100'] > 0]
    data_c['err/f *100'] = data_c['err/f *100'][data_c['err/f *100'] > 0]

    data_o['t'] = data_o['t'] + 2400000
    data_c['t'] = data_c['t'] + 2400000
    
    return data_o, data_c

def clean_atlas(data_o, data_c):
    data_o = data_o[(data_o['err/f *100']<10)]
    data_c = data_c[(data_c['err/f *100']<10)]


    data_o = data_o[data_o['log_redchi']<1.5]
    data_c = data_c[data_c['log_redchi']<1.5]

    data_o = data_o[ (data_o['m']>5) ]
    data_c = data_c[(data_c['m']>5) ]

    data_o = data_o.reset_index(drop=True)
    data_c = data_c.reset_index(drop=True)
    
    return data_o, data_c

def get_gaia_errors(mag):
    a1 = 0.2
    b1 = -5.2
    a2 = 0.26
    b2 = -6.26

    err = []
    for i in range(0, len(mag)):
        if mag[i] <= 13.5:
            err_corr = a1 * 13.5 + b1
        elif mag[i] > 13.5 and mag[i] <= 17.:
            err_corr = a1 * mag[i] + b1
        elif mag[i] > 17.:
            err_corr = a2 * mag[i] + b2
        err.append(10. ** err_corr)
    return err

def edit_gaia_file(path):
    data = pd.read_csv(path)


    data['averagemag'] = pd.to_numeric(data['averagemag'], errors='coerce')


    df_cleaned = data.dropna(subset=['averagemag'])
    df_cleaned.reset_index(drop=True, inplace=True)
    df_cleaned['err_mag'] = get_gaia_errors(df_cleaned['averagemag'])

    return df_cleaned
