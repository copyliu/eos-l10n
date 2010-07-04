#Copyright 2009 Diego Duclos
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Note: Only this file in this subfolder has this notice for practical reason
#(This notice is longer then most of the files)
#This notice however applies to every file in this folder.

#The function declaration of effects should be the following:
#def effectName(self, fitting):
#self: refers to the instance of the effect class the effect is bound to
#fitting: refers to the fit requesting attributes to be modified

#In addition, the following types take extra keyword arguments
#If an effect is part of multiple of those types
#it needs to accept any of those arguments
#Modules:
#    state: the state of the module, this can be offline, inactive, active, overloaded
#           for more information about states, check fitting.py

#Ammo: 
#    containerModule: The module this ammo is in

#Skills:
#    level: The level the skill is at