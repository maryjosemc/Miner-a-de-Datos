```python
conda install -c conda-forge/label/gcc7 missingno
```

    Collecting package metadata (current_repodata.json): ...working... done
    Solving environment: ...working... done
    
    ## Package Plan ##
    
      environment location: C:\Users\Mary\Anaconda3
    
      added / updated specs:
        - missingno
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        conda-4.8.2                |           py37_0         2.8 MB
        missingno-0.4.1            |             py_0          10 KB  conda-forge/label/gcc7
        ------------------------------------------------------------
                                               Total:         2.8 MB
    
    The following NEW packages will be INSTALLED:
    
      missingno          conda-forge/label/gcc7/noarch::missingno-0.4.1-py_0
    
    The following packages will be UPDATED:
    
      conda                                       4.7.12-py37_0 --> 4.8.2-py37_0
    
    
    
    Downloading and Extracting Packages
    
    missingno-0.4.1      | 10 KB     |            |   0% 
    missingno-0.4.1      | 10 KB     | ########## | 100% 
    
    conda-4.8.2          | 2.8 MB    |            |   0% 
    conda-4.8.2          | 2.8 MB    |            |   1% 
    conda-4.8.2          | 2.8 MB    | 6          |   7% 
    conda-4.8.2          | 2.8 MB    | 9          |  10% 
    conda-4.8.2          | 2.8 MB    | #3         |  13% 
    conda-4.8.2          | 2.8 MB    | #6         |  17% 
    conda-4.8.2          | 2.8 MB    | ##1        |  21% 
    conda-4.8.2          | 2.8 MB    | ##5        |  26% 
    conda-4.8.2          | 2.8 MB    | ##9        |  30% 
    conda-4.8.2          | 2.8 MB    | ###3       |  33% 
    conda-4.8.2          | 2.8 MB    | ###6       |  36% 
    conda-4.8.2          | 2.8 MB    | ###8       |  39% 
    conda-4.8.2          | 2.8 MB    | ####       |  41% 
    conda-4.8.2          | 2.8 MB    | ####2      |  42% 
    conda-4.8.2          | 2.8 MB    | ####6      |  46% 
    conda-4.8.2          | 2.8 MB    | ####7      |  47% 
    conda-4.8.2          | 2.8 MB    | ####8      |  48% 
    conda-4.8.2          | 2.8 MB    | #####      |  50% 
    conda-4.8.2          | 2.8 MB    | #####1     |  52% 
    conda-4.8.2          | 2.8 MB    | #####4     |  55% 
    conda-4.8.2          | 2.8 MB    | #####6     |  57% 
    conda-4.8.2          | 2.8 MB    | #####9     |  59% 
    conda-4.8.2          | 2.8 MB    | ######2    |  62% 
    conda-4.8.2          | 2.8 MB    | ######5    |  66% 
    conda-4.8.2          | 2.8 MB    | ######8    |  69% 
    conda-4.8.2          | 2.8 MB    | #######2   |  72% 
    conda-4.8.2          | 2.8 MB    | #######4   |  75% 
    conda-4.8.2          | 2.8 MB    | #######7   |  78% 
    conda-4.8.2          | 2.8 MB    | #######9   |  80% 
    conda-4.8.2          | 2.8 MB    | ########2  |  82% 
    conda-4.8.2          | 2.8 MB    | ########5  |  85% 
    conda-4.8.2          | 2.8 MB    | ########7  |  88% 
    conda-4.8.2          | 2.8 MB    | #########1 |  92% 
    conda-4.8.2          | 2.8 MB    | #########6 |  96% 
    conda-4.8.2          | 2.8 MB    | ########## | 100% 
    Preparing transaction: ...working... done
    Verifying transaction: ...working... done
    Executing transaction: ...working... done
    
    Note: you may need to restart the kernel to use updated packages.
    


```python

```


```python
import pandas as pd
import numpy as np
import missingno as msno
%matplotlib inline
```


```python
#D:\Documentos\MAC\Semestres\Octavo\Mineria de datos\Practicas\Practica1

path = 'D:\Documentos\MAC\Semestres\Octavo\Mineria de datos\Practicas\Practica1\concentradohogar.csv'
df = pd.read_csv(path, encoding='latin', error_bad_lines=False)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>100013601</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>100013602</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>147.54</td>
      <td>147.54</td>
      <td>0.0</td>
      <td>9.83</td>
      <td>0.0</td>
      <td>8852.45</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>100013603</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>66393.44</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>14754.09</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>100013604</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>100013606</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 126 columns</p>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 74647 entries, 0 to 74646
    Columns: 126 entries, folioviv to smg
    dtypes: float64(104), int64(22)
    memory usage: 71.8 MB
    


```python
df.shape
```




    (74647, 126)




```python
df.shape[0]
```




    74647




```python
df.shape[1]
```




    126




```python
df.columns.values.tolist()
```




    ['folioviv',
     'foliohog',
     'ubica_geo',
     'tam_loc',
     'est_socio',
     'est_dis',
     'upm',
     'factor',
     'clase_hog',
     'sexo_jefe',
     'edad_jefe',
     'educa_jefe',
     'tot_integ',
     'hombres',
     'mujeres',
     'mayores',
     'menores',
     'p12_64',
     'p65mas',
     'ocupados',
     'percep_ing',
     'perc_ocupa',
     'ing_cor',
     'ingtrab',
     'trabajo',
     'sueldos',
     'horas_extr',
     'comisiones',
     'aguinaldo',
     'indemtrab',
     'otra_rem',
     'remu_espec',
     'negocio',
     'noagrop',
     'industria',
     'comercio',
     'servicios',
     'agrope',
     'agricolas',
     'pecuarios',
     'reproducc',
     'pesca',
     'otros_trab',
     'rentas',
     'utilidad',
     'arrenda',
     'transfer',
     'jubilacion',
     'becas',
     'donativos',
     'remesas',
     'bene_gob',
     'transf_hog',
     'trans_inst',
     'estim_alqu',
     'otros_ing',
     'gasto_mon',
     'alimentos',
     'ali_dentro',
     'cereales',
     'carnes',
     'pescado',
     'leche',
     'huevo',
     'aceites',
     'tuberculo',
     'verduras',
     'frutas',
     'azucar',
     'cafe',
     'especias',
     'otros_alim',
     'bebidas',
     'ali_fuera',
     'tabaco',
     'vesti_calz',
     'vestido',
     'calzado',
     'vivienda',
     'alquiler',
     'pred_cons',
     'agua',
     'energia',
     'limpieza',
     'cuidados',
     'utensilios',
     'enseres',
     'salud',
     'atenc_ambu',
     'hospital',
     'medicinas',
     'transporte',
     'publico',
     'foraneo',
     'adqui_vehi',
     'mantenim',
     'refaccion',
     'combus',
     'comunica',
     'educa_espa',
     'educacion',
     'esparci',
     'paq_turist',
     'personales',
     'cuida_pers',
     'acces_pers',
     'otros_gas',
     'transf_gas',
     'percep_tot',
     'retiro_inv',
     'prestamos',
     'otras_perc',
     'ero_nm_viv',
     'ero_nm_hog',
     'erogac_tot',
     'cuota_viv',
     'mater_serv',
     'material',
     'servicio',
     'deposito',
     'prest_terc',
     'pago_tarje',
     'deudas',
     'balance',
     'otras_erog',
     'smg']




```python
df.dtypes
```




    folioviv        int64
    foliohog        int64
    ubica_geo       int64
    tam_loc         int64
    est_socio       int64
                   ...   
    pago_tarje    float64
    deudas        float64
    balance       float64
    otras_erog    float64
    smg           float64
    Length: 126, dtype: object




```python
df.isnull().any().any()
```




    False




```python
msno.matrix(df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1b50000eac8>




![png](output_11_1.png)



```python
df.isnull().any().any()
```




    False




```python
msno.bar(df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1b50ddc9408>




![png](output_13_1.png)



```python
df.replace({0 : np.nan}, inplace=True)
```


```python
df.isnull().any().any()
```




    True




```python
msno.matrix(df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1b50e362408>




![png](output_16_1.png)



```python
msno.bar(df)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1b50ec64e08>




![png](output_17_1.png)



```python
df.columns[df.isnull().any()].tolist()
```




    []




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>7.464700e+04</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>...</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>7.464700e+04</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>74647.000000</td>
      <td>7.464700e+04</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>1.615773e+09</td>
      <td>1.019438</td>
      <td>15940.896888</td>
      <td>2.541817</td>
      <td>2.056077</td>
      <td>255.363752</td>
      <td>4299.807306</td>
      <td>465.454981</td>
      <td>2.147923</td>
      <td>1.274304</td>
      <td>...</td>
      <td>323.263475</td>
      <td>202.252622</td>
      <td>121.010853</td>
      <td>1.908805e+03</td>
      <td>81.913280</td>
      <td>737.844243</td>
      <td>457.422984</td>
      <td>324.582644</td>
      <td>382.930763</td>
      <td>7.952400e+03</td>
    </tr>
    <tr>
      <td>std</td>
      <td>9.304964e+08</td>
      <td>0.160412</td>
      <td>9317.200448</td>
      <td>1.315537</td>
      <td>0.814108</td>
      <td>158.184490</td>
      <td>2412.214410</td>
      <td>484.839505</td>
      <td>0.628463</td>
      <td>0.446166</td>
      <td>...</td>
      <td>3839.180764</td>
      <td>2752.694816</td>
      <td>1769.963469</td>
      <td>1.844932e+04</td>
      <td>1197.824028</td>
      <td>5581.064048</td>
      <td>3221.133166</td>
      <td>3772.934932</td>
      <td>5487.282854</td>
      <td>1.115685e-08</td>
    </tr>
    <tr>
      <td>min</td>
      <td>1.000136e+08</td>
      <td>1.000000</td>
      <td>1001.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>9.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.952400e+03</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>8.046809e+08</td>
      <td>1.000000</td>
      <td>8019.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>119.000000</td>
      <td>2273.000000</td>
      <td>170.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.952400e+03</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>1.562232e+09</td>
      <td>1.000000</td>
      <td>15124.000000</td>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>248.000000</td>
      <td>4292.000000</td>
      <td>323.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.952400e+03</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>2.403852e+09</td>
      <td>1.000000</td>
      <td>24028.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>385.000000</td>
      <td>6385.000000</td>
      <td>595.000000</td>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.952400e+03</td>
    </tr>
    <tr>
      <td>max</td>
      <td>3.260799e+09</td>
      <td>5.000000</td>
      <td>32056.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>543.000000</td>
      <td>8395.000000</td>
      <td>6727.000000</td>
      <td>5.000000</td>
      <td>2.000000</td>
      <td>...</td>
      <td>537016.560000</td>
      <td>358011.040000</td>
      <td>179005.520000</td>
      <td>2.934783e+06</td>
      <td>124918.030000</td>
      <td>440217.390000</td>
      <td>433755.240000</td>
      <td>297132.060000</td>
      <td>586956.520000</td>
      <td>7.952400e+03</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 126 columns</p>
</div>




```python
df.loc[[0]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>100013601</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 126 columns</p>
</div>




```python
df.loc[40:45]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>40</td>
      <td>100068902</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>9</td>
      <td>147</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>3179.34</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>41</td>
      <td>100068904</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>9</td>
      <td>147</td>
      <td>3</td>
      <td>1</td>
      <td>...</td>
      <td>244.56</td>
      <td>244.56</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>42</td>
      <td>100068906</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>9</td>
      <td>147</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>43</td>
      <td>100069801</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>10</td>
      <td>168</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>44</td>
      <td>100069802</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>10</td>
      <td>168</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>45</td>
      <td>100069803</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>10</td>
      <td>168</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>7377.04</td>
      <td>0.0</td>
      <td>9590.16</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 126 columns</p>
</div>




```python
df.drop([0,24,51], axis=0).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>100013602</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>147.54</td>
      <td>147.54</td>
      <td>0.0</td>
      <td>9.83</td>
      <td>0.0</td>
      <td>8852.45</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>100013603</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>66393.44</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>14754.09</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>100013604</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>100013606</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>5</td>
      <td>100026701</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>189</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>14754.09</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 126 columns</p>
</div>




```python
df[100:].head() #df.tail(-100) )
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>100</td>
      <td>100104705</td>
      <td>2</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>19</td>
      <td>122</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>101</td>
      <td>100104706</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>19</td>
      <td>122</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>4573.76</td>
      <td>4180.32</td>
      <td>393.44</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>102</td>
      <td>100113501</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>20</td>
      <td>130</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>103</td>
      <td>100113502</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>20</td>
      <td>130</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4402.17</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>104</td>
      <td>100113503</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>20</td>
      <td>130</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 126 columns</p>
</div>




```python
df.mujeres.values
```




    array([1, 3, 1, ..., 4, 0, 1], dtype=int64)




```python
df['mujeres'].values
```




    array([1, 3, 1, ..., 4, 0, 1], dtype=int64)




```python
df.mujeres.unique
```




    <bound method Series.unique of 0        1
    1        3
    2        1
    3        1
    4        3
            ..
    74642    1
    74643    1
    74644    4
    74645    0
    74646    1
    Name: mujeres, Length: 74647, dtype: int64>




```python
df.mujeres.unique()
```




    array([ 1,  3,  2,  0,  6,  4,  5,  7,  8,  9, 10, 11, 12], dtype=int64)




```python
df.mujeres.value_counts()
```




    1     27721
    2     22284
    3     12118
    0      6095
    4      4375
    5      1365
    6       474
    7       153
    8        38
    9        12
    10        7
    11        4
    12        1
    Name: mujeres, dtype: int64




```python
df.agg(['count','size','nunique'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>...</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
    </tr>
    <tr>
      <td>size</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>...</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>73405</td>
      <td>5</td>
      <td>996</td>
      <td>4</td>
      <td>4</td>
      <td>543</td>
      <td>8377</td>
      <td>1747</td>
      <td>5</td>
      <td>2</td>
      <td>...</td>
      <td>2199</td>
      <td>1701</td>
      <td>523</td>
      <td>1897</td>
      <td>482</td>
      <td>1899</td>
      <td>1885</td>
      <td>3641</td>
      <td>1590</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 126 columns</p>
</div>




```python
df.groupby('mujeres').agg(['count','size','nunique']).stack()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
    <tr>
      <th>mujeres</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3" valign="top">0</td>
      <td>count</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>...</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
    </tr>
    <tr>
      <td>size</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>...</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
      <td>6095</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>6022</td>
      <td>5</td>
      <td>824</td>
      <td>4</td>
      <td>4</td>
      <td>489</td>
      <td>3723</td>
      <td>1218</td>
      <td>5</td>
      <td>1</td>
      <td>...</td>
      <td>347</td>
      <td>285</td>
      <td>115</td>
      <td>381</td>
      <td>107</td>
      <td>266</td>
      <td>208</td>
      <td>294</td>
      <td>203</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">1</td>
      <td>count</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>...</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
    </tr>
    <tr>
      <td>size</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>...</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
      <td>27721</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>27445</td>
      <td>5</td>
      <td>994</td>
      <td>4</td>
      <td>4</td>
      <td>542</td>
      <td>7522</td>
      <td>1657</td>
      <td>5</td>
      <td>2</td>
      <td>...</td>
      <td>1158</td>
      <td>900</td>
      <td>324</td>
      <td>1061</td>
      <td>242</td>
      <td>1023</td>
      <td>850</td>
      <td>1758</td>
      <td>740</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">2</td>
      <td>count</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>...</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
    </tr>
    <tr>
      <td>size</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>...</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
      <td>22284</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>22160</td>
      <td>5</td>
      <td>991</td>
      <td>4</td>
      <td>4</td>
      <td>542</td>
      <td>7061</td>
      <td>1605</td>
      <td>5</td>
      <td>2</td>
      <td>...</td>
      <td>1003</td>
      <td>799</td>
      <td>272</td>
      <td>977</td>
      <td>238</td>
      <td>889</td>
      <td>877</td>
      <td>1362</td>
      <td>707</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">3</td>
      <td>count</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>...</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
    </tr>
    <tr>
      <td>size</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>...</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
      <td>12118</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>12089</td>
      <td>4</td>
      <td>979</td>
      <td>4</td>
      <td>4</td>
      <td>532</td>
      <td>5467</td>
      <td>1432</td>
      <td>4</td>
      <td>2</td>
      <td>...</td>
      <td>624</td>
      <td>516</td>
      <td>194</td>
      <td>725</td>
      <td>175</td>
      <td>577</td>
      <td>564</td>
      <td>954</td>
      <td>465</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">4</td>
      <td>count</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>...</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
    </tr>
    <tr>
      <td>size</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>...</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
      <td>4375</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>4374</td>
      <td>4</td>
      <td>839</td>
      <td>4</td>
      <td>4</td>
      <td>479</td>
      <td>2922</td>
      <td>1067</td>
      <td>4</td>
      <td>2</td>
      <td>...</td>
      <td>320</td>
      <td>271</td>
      <td>101</td>
      <td>414</td>
      <td>78</td>
      <td>226</td>
      <td>294</td>
      <td>383</td>
      <td>197</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">5</td>
      <td>count</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>...</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
    </tr>
    <tr>
      <td>size</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>...</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>1365</td>
      <td>3</td>
      <td>538</td>
      <td>4</td>
      <td>4</td>
      <td>349</td>
      <td>1148</td>
      <td>658</td>
      <td>3</td>
      <td>2</td>
      <td>...</td>
      <td>125</td>
      <td>101</td>
      <td>45</td>
      <td>208</td>
      <td>42</td>
      <td>82</td>
      <td>130</td>
      <td>172</td>
      <td>77</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">6</td>
      <td>count</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>...</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
    </tr>
    <tr>
      <td>size</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>...</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>474</td>
      <td>2</td>
      <td>277</td>
      <td>4</td>
      <td>4</td>
      <td>200</td>
      <td>435</td>
      <td>342</td>
      <td>4</td>
      <td>2</td>
      <td>...</td>
      <td>37</td>
      <td>31</td>
      <td>13</td>
      <td>90</td>
      <td>13</td>
      <td>29</td>
      <td>58</td>
      <td>56</td>
      <td>29</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">7</td>
      <td>count</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>...</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
    </tr>
    <tr>
      <td>size</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>...</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>153</td>
      <td>2</td>
      <td>115</td>
      <td>4</td>
      <td>3</td>
      <td>106</td>
      <td>151</td>
      <td>137</td>
      <td>3</td>
      <td>2</td>
      <td>...</td>
      <td>16</td>
      <td>14</td>
      <td>5</td>
      <td>41</td>
      <td>5</td>
      <td>11</td>
      <td>19</td>
      <td>27</td>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">8</td>
      <td>count</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>...</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
    </tr>
    <tr>
      <td>size</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>...</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>38</td>
      <td>1</td>
      <td>37</td>
      <td>4</td>
      <td>3</td>
      <td>32</td>
      <td>38</td>
      <td>38</td>
      <td>3</td>
      <td>2</td>
      <td>...</td>
      <td>8</td>
      <td>8</td>
      <td>5</td>
      <td>16</td>
      <td>3</td>
      <td>5</td>
      <td>10</td>
      <td>6</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">9</td>
      <td>count</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>...</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <td>size</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>...</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>4</td>
      <td>2</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>8</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">10</td>
      <td>count</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>...</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <td>size</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>...</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>2</td>
      <td>2</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">11</td>
      <td>count</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>...</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td>size</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>...</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">12</td>
      <td>count</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>size</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>39 rows × 125 columns</p>
</div>




```python
df.groupby('mujeres').agg(['count','size','nunique'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">folioviv</th>
      <th colspan="3" halign="left">foliohog</th>
      <th colspan="3" halign="left">ubica_geo</th>
      <th>tam_loc</th>
      <th>...</th>
      <th>deudas</th>
      <th colspan="3" halign="left">balance</th>
      <th colspan="3" halign="left">otras_erog</th>
      <th colspan="3" halign="left">smg</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>size</th>
      <th>nunique</th>
      <th>count</th>
      <th>size</th>
      <th>nunique</th>
      <th>count</th>
      <th>size</th>
      <th>nunique</th>
      <th>count</th>
      <th>...</th>
      <th>nunique</th>
      <th>count</th>
      <th>size</th>
      <th>nunique</th>
      <th>count</th>
      <th>size</th>
      <th>nunique</th>
      <th>count</th>
      <th>size</th>
      <th>nunique</th>
    </tr>
    <tr>
      <th>mujeres</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>6095</td>
      <td>6095</td>
      <td>6022</td>
      <td>6095</td>
      <td>6095</td>
      <td>5</td>
      <td>6095</td>
      <td>6095</td>
      <td>824</td>
      <td>6095</td>
      <td>...</td>
      <td>208</td>
      <td>6095</td>
      <td>6095</td>
      <td>294</td>
      <td>6095</td>
      <td>6095</td>
      <td>203</td>
      <td>6095</td>
      <td>6095</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>27721</td>
      <td>27721</td>
      <td>27445</td>
      <td>27721</td>
      <td>27721</td>
      <td>5</td>
      <td>27721</td>
      <td>27721</td>
      <td>994</td>
      <td>27721</td>
      <td>...</td>
      <td>850</td>
      <td>27721</td>
      <td>27721</td>
      <td>1758</td>
      <td>27721</td>
      <td>27721</td>
      <td>740</td>
      <td>27721</td>
      <td>27721</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>22284</td>
      <td>22284</td>
      <td>22160</td>
      <td>22284</td>
      <td>22284</td>
      <td>5</td>
      <td>22284</td>
      <td>22284</td>
      <td>991</td>
      <td>22284</td>
      <td>...</td>
      <td>877</td>
      <td>22284</td>
      <td>22284</td>
      <td>1362</td>
      <td>22284</td>
      <td>22284</td>
      <td>707</td>
      <td>22284</td>
      <td>22284</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>12118</td>
      <td>12118</td>
      <td>12089</td>
      <td>12118</td>
      <td>12118</td>
      <td>4</td>
      <td>12118</td>
      <td>12118</td>
      <td>979</td>
      <td>12118</td>
      <td>...</td>
      <td>564</td>
      <td>12118</td>
      <td>12118</td>
      <td>954</td>
      <td>12118</td>
      <td>12118</td>
      <td>465</td>
      <td>12118</td>
      <td>12118</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4375</td>
      <td>4375</td>
      <td>4374</td>
      <td>4375</td>
      <td>4375</td>
      <td>4</td>
      <td>4375</td>
      <td>4375</td>
      <td>839</td>
      <td>4375</td>
      <td>...</td>
      <td>294</td>
      <td>4375</td>
      <td>4375</td>
      <td>383</td>
      <td>4375</td>
      <td>4375</td>
      <td>197</td>
      <td>4375</td>
      <td>4375</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>1365</td>
      <td>3</td>
      <td>1365</td>
      <td>1365</td>
      <td>538</td>
      <td>1365</td>
      <td>...</td>
      <td>130</td>
      <td>1365</td>
      <td>1365</td>
      <td>172</td>
      <td>1365</td>
      <td>1365</td>
      <td>77</td>
      <td>1365</td>
      <td>1365</td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>474</td>
      <td>2</td>
      <td>474</td>
      <td>474</td>
      <td>277</td>
      <td>474</td>
      <td>...</td>
      <td>58</td>
      <td>474</td>
      <td>474</td>
      <td>56</td>
      <td>474</td>
      <td>474</td>
      <td>29</td>
      <td>474</td>
      <td>474</td>
      <td>1</td>
    </tr>
    <tr>
      <td>7</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>153</td>
      <td>2</td>
      <td>153</td>
      <td>153</td>
      <td>115</td>
      <td>153</td>
      <td>...</td>
      <td>19</td>
      <td>153</td>
      <td>153</td>
      <td>27</td>
      <td>153</td>
      <td>153</td>
      <td>9</td>
      <td>153</td>
      <td>153</td>
      <td>1</td>
    </tr>
    <tr>
      <td>8</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>1</td>
      <td>38</td>
      <td>38</td>
      <td>37</td>
      <td>38</td>
      <td>...</td>
      <td>10</td>
      <td>38</td>
      <td>38</td>
      <td>6</td>
      <td>38</td>
      <td>38</td>
      <td>5</td>
      <td>38</td>
      <td>38</td>
      <td>1</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>...</td>
      <td>3</td>
      <td>12</td>
      <td>12</td>
      <td>3</td>
      <td>12</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>12</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>...</td>
      <td>3</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
    </tr>
    <tr>
      <td>11</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>...</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <td>12</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>13 rows × 375 columns</p>
</div>




```python
df_sample = df.sample(frac=0.05, random_state=1)
df_sample.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>25744</td>
      <td>1060595612</td>
      <td>1</td>
      <td>10036</td>
      <td>4</td>
      <td>2</td>
      <td>155</td>
      <td>3129</td>
      <td>141</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>2065.57</td>
      <td>0.00</td>
      <td>1471.47</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>59296</td>
      <td>2504926523</td>
      <td>1</td>
      <td>25007</td>
      <td>3</td>
      <td>2</td>
      <td>404</td>
      <td>6776</td>
      <td>311</td>
      <td>3</td>
      <td>2</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>54678</td>
      <td>2360003820</td>
      <td>1</td>
      <td>23002</td>
      <td>4</td>
      <td>2</td>
      <td>376</td>
      <td>6189</td>
      <td>191</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>319.67</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>9199</td>
      <td>401315704</td>
      <td>1</td>
      <td>4003</td>
      <td>3</td>
      <td>1</td>
      <td>51</td>
      <td>1043</td>
      <td>167</td>
      <td>3</td>
      <td>2</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1180.32</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>69453</td>
      <td>3062418322</td>
      <td>1</td>
      <td>30128</td>
      <td>4</td>
      <td>1</td>
      <td>515</td>
      <td>7918</td>
      <td>694</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 126 columns</p>
</div>




```python
df.shape
```




    (74647, 126)




```python
df_sample.shape
```




    (3732, 126)




```python
#Transformación de los datos
df_dropped = df.dropna(subset=['ubica_geo'])
df_dropped.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>100013601</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>100013602</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>147.54</td>
      <td>147.54</td>
      <td>0.0</td>
      <td>9.83</td>
      <td>0.0</td>
      <td>8852.45</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>100013603</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>66393.44</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>14754.09</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>100013604</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>100013606</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 126 columns</p>
</div>




```python
df_dropped.shape
```




    (74647, 126)




```python
df_copy = df.copy()
df_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>100013601</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>100013602</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>147.54</td>
      <td>147.54</td>
      <td>0.0</td>
      <td>9.83</td>
      <td>0.0</td>
      <td>8852.45</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>100013603</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>1</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>66393.44</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>14754.09</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>100013604</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>100013606</td>
      <td>1</td>
      <td>1001</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>175</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 126 columns</p>
</div>




```python
df_copy.shape
```




    (74647, 126)




```python
#Rellenar valores faltantes con la media
df_dropped['deudas'].dtype
```




    dtype('float64')




```python
df_dropped['deudas'].mean()
```




    457.4229840449028




```python
df_copy['deudas'].fillna(value=np.round(df['deudas'].mean(),decimals=0),inplace=True)
```


```python
df_copy.agg(['count','size','nunique'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>...</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
    </tr>
    <tr>
      <td>size</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>...</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
      <td>74647</td>
    </tr>
    <tr>
      <td>nunique</td>
      <td>73405</td>
      <td>5</td>
      <td>996</td>
      <td>4</td>
      <td>4</td>
      <td>543</td>
      <td>8377</td>
      <td>1747</td>
      <td>5</td>
      <td>2</td>
      <td>...</td>
      <td>2199</td>
      <td>1701</td>
      <td>523</td>
      <td>1897</td>
      <td>482</td>
      <td>1899</td>
      <td>1885</td>
      <td>3641</td>
      <td>1590</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 126 columns</p>
</div>




```python
#Resumen de datos


```


```python
df_copy['deudas'].mean()
```




    457.4229840449028




```python
df_copy['deudas'][df_copy['rentas'] == 1].mean()
```




    nan




```python
df_copy['tot_integ'].mean()
```




    3.6044985063029995




```python
df_copy['tot_integ'][df_copy['mujeres'] == 1].mean()
```




    2.5870639587316475




```python
df_copy['deudas'][df_copy['rentas'] == 1]
```




    Series([], Name: deudas, dtype: float64)




```python
df_copy.groupby(["ubica_geo", "negocio", "rentas"]).count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>edad_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
    <tr>
      <th>ubica_geo</th>
      <th>negocio</th>
      <th>rentas</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5" valign="top">1001</td>
      <td rowspan="5" valign="top">0.00</td>
      <td>0.00</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>...</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
      <td>934</td>
    </tr>
    <tr>
      <td>24.86</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>220.10</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>586.95</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>880.43</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td rowspan="5" valign="top">32056</td>
      <td>25128.68</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>25377.04</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>26168.47</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>31793.47</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>51834.13</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>27480 rows × 123 columns</p>
</div>




```python
df_copy.groupby(["ubica_geo", "negocio"])[["rentas"]].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>rentas</th>
    </tr>
    <tr>
      <th>ubica_geo</th>
      <th>negocio</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5" valign="top">1001</td>
      <td>0.00</td>
      <td>1097</td>
    </tr>
    <tr>
      <td>74.34</td>
      <td>1</td>
    </tr>
    <tr>
      <td>99.44</td>
      <td>1</td>
    </tr>
    <tr>
      <td>122.28</td>
      <td>1</td>
    </tr>
    <tr>
      <td>162.29</td>
      <td>1</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td rowspan="5" valign="top">32056</td>
      <td>25128.68</td>
      <td>1</td>
    </tr>
    <tr>
      <td>25377.04</td>
      <td>1</td>
    </tr>
    <tr>
      <td>26168.47</td>
      <td>1</td>
    </tr>
    <tr>
      <td>31793.47</td>
      <td>1</td>
    </tr>
    <tr>
      <td>51834.13</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>23099 rows × 1 columns</p>
</div>




```python
df_copy.ubica_geo
```




    0         1001
    1         1001
    2         1001
    3         1001
    4         1001
             ...  
    74642    32046
    74643    32046
    74644    32046
    74645    32046
    74646    32046
    Name: ubica_geo, Length: 74647, dtype: int64




```python
df_sample = df.sample(frac=0.05, random_state=1)
df_sample.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>folioviv</th>
      <th>foliohog</th>
      <th>ubica_geo</th>
      <th>tam_loc</th>
      <th>est_socio</th>
      <th>est_dis</th>
      <th>upm</th>
      <th>factor</th>
      <th>clase_hog</th>
      <th>sexo_jefe</th>
      <th>...</th>
      <th>mater_serv</th>
      <th>material</th>
      <th>servicio</th>
      <th>deposito</th>
      <th>prest_terc</th>
      <th>pago_tarje</th>
      <th>deudas</th>
      <th>balance</th>
      <th>otras_erog</th>
      <th>smg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>25744</td>
      <td>1.060596e+09</td>
      <td>1.0</td>
      <td>10036.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>155.0</td>
      <td>3129.0</td>
      <td>141.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2065.57</td>
      <td>NaN</td>
      <td>1471.47</td>
      <td>NaN</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>59296</td>
      <td>2.504927e+09</td>
      <td>1.0</td>
      <td>25007.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>404.0</td>
      <td>6776.0</td>
      <td>311.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>54678</td>
      <td>2.360004e+09</td>
      <td>1.0</td>
      <td>23002.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>376.0</td>
      <td>6189.0</td>
      <td>191.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>319.67</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>9199</td>
      <td>4.013157e+08</td>
      <td>1.0</td>
      <td>4003.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>51.0</td>
      <td>1043.0</td>
      <td>167.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1180.32</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7952.4</td>
    </tr>
    <tr>
      <td>69453</td>
      <td>3.062418e+09</td>
      <td>1.0</td>
      <td>30128.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>515.0</td>
      <td>7918.0</td>
      <td>694.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7952.4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 126 columns</p>
</div>




```python
df_sample.groupby(["ubica_geo", "negocio"])[["rentas"]].agg([np.sum, np.mean,
                                                              np.count_nonzero])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3" halign="left">rentas</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>sum</th>
      <th>mean</th>
      <th>count_nonzero</th>
    </tr>
    <tr>
      <th>ubica_geo</th>
      <th>negocio</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4" valign="top">1001.0</td>
      <td>162.29</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>5121.54</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>25620.65</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>44139.13</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>1003.0</td>
      <td>880.43</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>32051.0</td>
      <td>19481.08</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">32053.0</td>
      <td>921.52</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>6356.73</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>15686.55</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>32056.0</td>
      <td>12690.49</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>1107 rows × 3 columns</p>
</div>




```python
df_sample.groupby(["ubica_geo", "negocio"]).agg({'vivienda':np.mean,'alquiler':np.max})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>vivienda</th>
      <th>alquiler</th>
    </tr>
    <tr>
      <th>ubica_geo</th>
      <th>negocio</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4" valign="top">1001.0</td>
      <td>162.29</td>
      <td>345.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>5121.54</td>
      <td>165.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>25620.65</td>
      <td>3750.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>44139.13</td>
      <td>869.19</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>1003.0</td>
      <td>880.43</td>
      <td>405.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>32051.0</td>
      <td>19481.08</td>
      <td>1866.28</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td rowspan="3" valign="top">32053.0</td>
      <td>921.52</td>
      <td>679.16</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>6356.73</td>
      <td>1175.80</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>15686.55</td>
      <td>1500.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>32056.0</td>
      <td>12690.49</td>
      <td>6150.00</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1107 rows × 2 columns</p>
</div>




```python
df_sample['ubica_geo'] = df_sample['ubica_geo'].astype('int64')

df_sample.plot(kind='scatter',x='deudas',y='percep_ing')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1b50f49da48>




![png](output_55_1.png)



```python
#Histogramas
plt.hist(df_sample['ubica_geo'])
plt.xlabel('ubica_geo')
plt.ylabel('Frequency')
plt.title('Frequency of ubica_geo')

```




    Text(0.5, 1.0, 'Frequency of ubica_geo')




![png](output_56_1.png)



```python
plt.hist(df_sample['mujeres'])
plt.xlabel('mujeres')
plt.ylabel('Frequency')
plt.title('Frequency of mujeres')
```




    Text(0.5, 1.0, 'Frequency of mujeres')




![png](output_57_1.png)



```python
plt.hist(df_sample['gasto_mon'])
plt.xlabel('gasto_mon')
plt.ylabel('Frequency')
plt.title('Frequency of gasto_mon')
```




    Text(0.5, 1.0, 'Frequency of gasto_mon')




![png](output_58_1.png)



```python
#Quartiles
plt.boxplot(df_sample['edad_jefe'], showmeans=True, meanline=True)
plt.ylabel('edad_jefe count')
plt.title('Box Plot of edad_jefe')
```




    Text(0.5, 1.0, 'Box Plot of edad_jefe')




![png](output_59_1.png)



```python

```
