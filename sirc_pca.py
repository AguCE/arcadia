# Function definition is here
def sirc_pca( file):
    "Analysis to explore which features explain the behaviour of the data"
    df=pd.read_excel(file)
    #Data cleaning
    le = preprocessing.LabelEncoder()
    #Data
    dfx=df.drop(['Resultado','Muestra'],axis=1)
    x=dfx.values
    xn=StandardScaler().fit_transform(x)
    #Code
    cod=df.Muestra
    #Feature name
    f= list(dfx)
    #Number of features
    nf=len(f)
    #Labels
    y=df.Resultado
    #target
    y_c=le.fit_transform(y)
    #Unique target
    target_number=np.unique(y_c)
    #Unique labels
    target_names=y.unique()
    #Number of labels
    nl=len(target_names)
    data_set={'data':x, 
              'data_normalized':xn,
              'code': cod,
              'target':y_c,
              'labels':y,
              'unique labels': target_names,
              'len':nl,
              'feature': f,
              'len_f': nf}
    
    #Calculo de la Matriz de Covarianza de las variables
    cov_mat = np.cov(xn.T)
    #Calculo de los Eigenvalues and Eigenvector
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)

   
    ev_ab=abs(eig_vals)
    ev_t=sum(ev_ab)
    var_exp=[(i / ev_t)*100 for i in ev_ab]

    df_fi=pd.DataFrame({
    'feature':f,
    'eigen_value':eig_vals,
    'var_explain':var_exp
    })

    df_fi=df_fi.sort_values(by='var_explain', ascending=False)

    df_fi['var_acu']=df_fi['var_explain'].cumsum()
    
    #To select feature that represent the 90%:
    dfvi=df_fi.loc[df_fi['var_acu'] <= 91]
    
    #PCA
    pca = PCA(n_components=2)
    X_r = pca.fit(xn).transform(xn)
    data_final=pd.DataFrame(data_set['data'], columns=data_set['feature'])
    data_final['Resultado']=pd.DataFrame(data_set['labels'])
    data_final['Muestra']=pd.DataFrame(data_set['code'])
    PC=pd.DataFrame(X_r, columns=['PC1','PC2'])
    data_final=data_final.join(PC)
    
    file="sirc_pca.xlsx"
    with pd.ExcelWriter(file) as writer:
        pd.DataFrame(cov_mat).to_excel(writer, sheet_name='cov_mat')
        df_fi.to_excel(writer, sheet_name='feature_var')
        dfvi.to_excel(writer, sheet_name='feature 09')
        data_final.to_excel(writer, sheet_name='PCA')
    print('Analisys done!')
    return;
