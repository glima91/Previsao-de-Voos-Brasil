import os
import pandas as pd
import csv

def Time_Parser(texto): 
    texto = texto.replace(".","/")
    Atexto = texto.split(" ")
    for i in range(len(Atexto)):
        if i ==0: 
            
            Adata = Atexto[0].split("/")
            #print(Adata)    
            dia = int(Adata[0])
            mes = int(Adata[1])
            ano = int(Adata[2])
    
        if i != 0 and Atexto[i].strip() != "":
            Ahora = Atexto[i].split(":")
            hora = Ahora[0]
            minuto = Ahora[1]
    
    #print("Dia:",dia," Mês:",mes," Ano:",ano," Hora:",hora, "Min:",minuto)

    return dia,mes,ano,hora,minuto





def read_files():
    #local do script python
    folder_path = os.path.dirname(os.path.realpath(__file__)) 
    
     

    file_output = open(folder_path + "/Processamento/Saida.csv",'w')
    
    texto_teste = ""
    texto_previsao_origem = ""
    texto_previsao_destino = ""
    cabecalho_previsao = ""
    with open(folder_path + "/Processamento/Voos.csv", "r") as f:
        reader = csv.reader(f, delimiter=";")
        # percorre linhas
        for i, line in enumerate(reader):
            
              

            texto_saida = ""
            # percorre cada coluna de uma linha
            for k in range(len(line)):
                
                texto_saida += line[k] + ";"
                # Campo "Partida Prevista"
                if k==6 and i != 0 and line[k] != "":
                    # data do voo
                    voo_dia, voo_mes, voo_ano, voo_hora, voo_min = Time_Parser(line[k])

                    icao_origem = line[4]
                    icao_destino = line[5]
                    # Abre

                    delta_hora = 24
                    
                    
                    with open(folder_path + "/Processamento/"+ icao_origem +".csv", "r") as f2:
                        reader_2 = csv.reader(f2, delimiter=";")
                        texto_previsao_origem = ""
                        for i_2, line_2 in enumerate(reader_2):

                            # percorre cada coluna de uma linha    
                            for k_2 in range(len(line_2)):   
                                

                                
                                # Campo "Hora local em aeroporto" 
                                if k_2==0 and i_2 != 0 and line_2[k_2] != "":
                                    # data previsao do tempo
                                    #print(line_2[k_2]) 
                                    prev_dia, prev_mes, prev_ano, prev_hora, prev_min = Time_Parser(line_2[k_2])   

                                    if voo_dia == prev_dia and voo_mes == prev_mes and voo_ano == prev_ano: 
                                        #print(voo_hora)
                                        #print(prev_hora)
                                        delta_hora_novo = int(voo_hora) - int(prev_hora)
                                        delta_hora_novo = abs(delta_hora_novo)
                                        if delta_hora > delta_hora_novo:
                                            delta_hora = delta_hora_novo
                                            linha_previsao = line_2
                                            i_previsao = i_2
                            
                    #obte dados da linha de previsao do tempo compativel 
                    #print(linha_previsao)  
                    for j in range(len(linha_previsao)):
                        texto_previsao_origem += linha_previsao[j] + ";" 

                    

                    delta_hora = 24
                    
                    
                    with open(folder_path + "/Processamento/"+ icao_destino +".csv", "r") as f2:
                        reader_2 = csv.reader(f2, delimiter=";")
                        texto_previsao_destino = ""
                        for i_2, line_2 in enumerate(reader_2):

                            # percorre cada coluna de uma linha    
                            for k_2 in range(len(line_2)):   
                                

                                
                                # Campo "Hora local em aeroporto" 
                                if k_2==0 and i_2 != 0 and line_2[k_2] != "":
                                    # data previsao do tempo
                                    #print(line_2[k_2]) 
                                    prev_dia, prev_mes, prev_ano, prev_hora, prev_min = Time_Parser(line_2[k_2])   

                                    if voo_dia == prev_dia and voo_mes == prev_mes and voo_ano == prev_ano: 
                                        #print(voo_hora)
                                        #print(prev_hora)
                                        delta_hora_novo = int(voo_hora) - int(prev_hora)
                                        delta_hora_novo = abs(delta_hora_novo)
                                        if delta_hora > delta_hora_novo:
                                            delta_hora = delta_hora_novo
                                            linha_previsao = line_2
                                            i_previsao = i_2
                            
                    #obte dados da linha de previsao do tempo compativel 
                    #print(linha_previsao)  
                    for j in range(len(linha_previsao)):
                        texto_previsao_destino += linha_previsao[j] + ";" 







            #cria cabeçalho    
            if i!=0:
                texto_saida = texto_saida +  texto_previsao_origem  + texto_previsao_destino
            else:
                texto_saida = "ICAO Empresa Aérea;Número Voo;Código Autorização (DI);Código Tipo Linha;ICAO Aeródromo Origem;ICAO Aeródromo Destino;Partida Prevista;Partida Real;Chegada Prevista;Chegada Real;Situação Voo;Código Justificativa;Previsão do Tempo;Hora local;T;Po;P;Pa;U;DD;Ff;ff10;ff3;N;WW;W1;W2;Tn;Tx;Cl;Nh;H;Cm;Ch;VV;Td;RRR;tR;E;Tg;E';sss;Hora local;T;Po;P;Pa;U;DD;Ff;ff10;ff3;N;WW;W1;W2;Tn;Tx;Cl;Nh;H;Cm;Ch;VV;Td;RRR;tR;E;Tg;E';sss" + "\n"
                    
            # Dados de previsao do tempo
            print("Linha lida: ",i) 
            
            #print(texto_teste)           
            # retira ultimo caractere
            texto_saida = texto_saida[:-1]
            texto_saida += "\n"
            
            #print(texto_saida) 
            file_output.write(texto_saida)
                
    file_output.close()
    return
    


if __name__ == "__main__":
    read_files()  
    print("PROCESSO CONCLUIDO!")  



