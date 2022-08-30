# -*- coding: utf-8 -*-

from os import listdir

pasta = r'Caminho'

def listar_arquivos(pasta, ignora_abertos = True):
    '''
    Cria uma lista com arquivos e pastas existentes no caminho fornecido.
    
    Parameters
    ----------
    pasta : str
        Caminho completo da pasta a verificar.
    ignora_abertos : bool, optional
        Para ignorar ou não temporários gerados na abertura de um arquivo.
        The default is True.

    Returns
    -------
    lista : lista
        Lista com conteúdo.
    '''
    if ignora_abertos:
        lista = [item for item in listdir(pasta) if '$' not in item]
    else:
        lista = [item for item in listdir(pasta)]
    return lista

lista_de_arquivos = listar_arquivos(pasta, False)