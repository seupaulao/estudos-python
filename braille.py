#!/usr/bin/python
## -*- coding: utf-8 -*-

# inicio 10240
# fim 10303
# 10241 a
# 10243 b
# 10249 c
# 10265 d
# 10274 e
# 10251 f
# 10267 g
# 10259 h
# 10250 i
# 10266 j
# 10242 k
# 10247 l
# 10253 m
# 10269 n
# 10261 o
# 10255 p
# 10271 q
# 10263 r
# 10254 s
# 10270 t
# 10277 u
# 10279 v
# 10285 x
# 10301 y
# 10293 z
# 10240 espaco
# 10287 ç
# 10295 á
# 10303 é
# 10252 í
# 10284 ó
# 10302 ú
# 10268 ã
# 10282 õ
# 10283 à
alfab1=[10241,10243,10249,10265,10257,10251,10267,10259,10250,10266,10242,10247,10253,10269,10261,10255,10271,10263,10254,10270,10277,10279,10285,10301,10293,10240,10287,10295,10303,10252,10284,10302,10268,10282,10283]
alfab2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z',' ','ç','á','é','í','ó','ú','ã','õ','à']

def laco1():
   x = 10239
   for i in range(64):
       x += 1
       print i, x, "...............",unichr(x)

def laco2():
   for i in range(len(alfab2)):
       print i, alfab2[i], alfab1[i], unichr(alfab1[i]) 


def traduz(frase):
   total = ''
   for i in range(len(frase)):
      try:
         p = alfab2.index(frase[i])  
      except:
         p = -1
      if p >= 0:
         total = total + unichr(alfab1[p])
   print total

traduz('eis a frase')
traduz('o pai do puxasaco')
traduz('nada poderá me deter')
traduz('o super ferrolho')
traduz('é mais que um coração')











