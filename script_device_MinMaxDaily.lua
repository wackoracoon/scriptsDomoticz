commandArray = {}
if devicechanged['Temperature Bureau'] then
        temp = otherdevices_svalues['Temperature Bureau']
        
        storedMin = tonumber(otherdevices_svalues["TempMin"])
        storedMax = tonumber(otherdevices_svalues["TempMax"])
        actualTemp = tonumber(temp)
        if ( actualTemp > storedMax ) then
                commandArray['UpdateDevice']='184|0|'..actualTemp..''
        elseif ( actualTemp < storedMin ) then
                commandArray['UpdateDevice']='183|0|'..actualTemp..''
        end
end
return commandArray
