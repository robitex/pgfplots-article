--[[
  
   Copyright (C) 2011 Agostino De Marco
                      <agostino dot demarco at unina dot it>
                      Roberto Giacomelli
                      <giaconet dot mailbox at gmail dot com>
  
      This work may be distributed and/or modified under the
      conditions of the LaTeX Project Public License, either
      version 1.3 of this license or any later version.
      The latest version of this license is in
      http://www.latex-project.org/lppl.txt and version 1.3
      or later is part of all distributions of LaTeX version
      2005/12/01 or later.
  
   This work has the LPPL maintenance status `maintained'.
   
   The Current Maintainer of this work are Agostino De Marco
   and Roberto Giacomelli
  
--]]

--[[
     Curve di Eulero-Johnson per vari valori
     del carico di snervamento del materiale
--]]

-- funzione ausiliaria scrittura dati
local function formatData(x,y)
   return string.format("%.2f\t%.3f",x,y)
end

-- funzione ausiliaria creazione file
local function makefile(fn,t)
   local outputfile = assert(io.open(fn,"w"))
   outputfile:write(table.concat(t,"\n"))
   outputfile:close()
end

-- Modulo di Young (daN/mm^2)
local EY = 7200

-- intervallo di calcolo e numero di suddivisioni
local Lmin, Lmax, n = 0, 100, 1000
local step = (Lmax-Lmin)/n

-- tabella dati di transizione
local points = {}

for ss=20,90,10 do
   -- tabella temporanea dati
   local t = {}
   
   -- lunghezza di transizione
   local Lt = math.pi*math.sqrt(2*EY/ss)
   
   -- passi fino a non superare Lt
   local Ltlim = math.floor((Lt-Lmin)/step)
   
   -- Rottura alla Johnson
   for i = 0, Ltlim do
      local L = Lmin + i*step
      local J =ss*(1-(L^2)/(4*math.pi^2*EY)*ss)
      t[#t+1] = formatData(L,J)
   end
   
   points[#points+1] =
            formatData(Lt,(math.pi^2*EY)/(Lt^2))
   
   -- Rottura alla Eulero
   for i = Ltlim+1, n do
      local L = Lmin + i*step
      local E =(math.pi^2*EY)/(L^2)
      t[#t+1] = formatData(L,E)
   end
   
   -- scrittura della tabella su file esterno
   makefile("dati"..tostring(ss)..".txt", t)
end

makefile("points.txt", points)