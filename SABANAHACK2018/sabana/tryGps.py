
import numpy as np
from geopy.geocoders import GoogleV3
import matplotlib.pyplot as plt
import math as mh

def get_component(location, component_type):
    for component in location.raw['address_components']:
        if component_type in component['types']:
            return component['long_name']
    """
        Peticiones por

        country = get_component(address, 'country')
        admin1 = get_component(address, 'administrative_area_level_1')
        admin2 = get_component(address, 'administrative_area_level_2')

        country = get_component(GL, 'country')
        admin1 = get_component(GL, 'administrative_area_level_1')
        admin2 = get_component(GL, 'administrative_area_level_2')
        direccion = get_component(GL, 'formatted_address')
        placerino = get_component(GL, 'place_id')
    """


def GL_to_dir(lat, longit):
    pointx = lat
    pointy = longit
    point = str(pointx)+','+str(pointy)
    geolocator = GoogleV3(api_key="AIzaSyC7ptlYha7iHq9yuHKQ09wLJm1kAYtoSm8")
    address = geolocator.reverse(point, exactly_one=True)
    print(address[0])


def dir_to_GL(dir, dpto, localidad):
    geolocator = GoogleV3(api_key="AIzaSyC7ptlYha7iHq9yuHKQ09wLJm1kAYtoSm8")
    GL=geolocator.geocode(dir,components={'administrative_area_level_1':str(dpto),'administrative_area_level_2':str(localidad)})
    print(GL)



def refrescar(archivo, pings):

    found = pings[:,2]
    MAC = archivo[:,9]
    new_archivo = archivo
    for i in range(len(MAC)):
        for j in range(len(found)):


            #Revisar aquí
            if (i == 34 and (j==3 or j==4 or j==5)):
                print( ''.join(pings[j,2]) is ''.join(archivo[i,9])  )
                print( ''.join(pings[j,2]), ''.join(archivo[i,9])  )

            if (i!=0 and pings[j,2] is archivo[i,9].split('"')[1]):
                nlat_old = archivo[i,2].split(' ')[0].split(':')[1]
                nlon_old = archivo[i,2].split(' ')[1].split(':')[1]
                nlat_new = pings[j,0].split(' ')[0].split(':')[1]
                nlon_new = pings[j,0].split(' ')[1].split(':')[1]

                lat_old = float(nlat_old)
                lon_old = float(nlon_old)
                lat_new = float(nlat_new)
                lon_new = float(nlon_new)

                send_lat = (lat_old*archivo[i,10] + lat_new)/(archivo[i,10]+1.0)
                send_lon = (lon_old*archivo[i,10] + lon_new)/(archivo[i,10]+1.0)

                print('hice algo')

                new_archivo[i,10]+=1

                new_archivo[i,0] = 'LAT:'+str(send_lat)+' LON:'+str(send_lon)
            elif():
                print (naaaaaa)
    return new_archivo



ar_mod = np.loadtxt('mod.csv', delimiter=',', dtype=str, comments = None)
ar_lecturas = np.loadtxt('lecturas.csv', delimiter=',', dtype=str, comments=None)
mod1_new = refrescar(ar_mod, ar_lecturas)
np.savetxt('mod1.txt',mod1_new, delimiter=',', fmt='%s')
print(mod1_new[:,10])



def graficas():
    k=np.array([1,50,100,150,300])
    N_old=np.array([0,1,50,100,150])

    errores = []
    totales = []
    dentrox = []
    dentroy = []
    circleAngle = np.linspace(0,2*np.pi,500)
    circlex = np.cos(circleAngle)
    circley = np.sin(circleAngle)
    for i in range(len(k)):
        N=k[i]
        N_viejo = N_old[i]
        con = N-N_viejo

        for j in range(con):
            a = 2*(np.random.random() -0.5)
            b = 2*(np.random.random() -0.5)

            if ( np.sqrt(np.power(a, 2) + np.power(b,2)) < 1):
                dentrox.append(a)
                dentroy.append(b)

        promx = float(np.mean(dentrox))
        promy = float(np.mean(dentroy))

        rad = np.sqrt(np.power(promx, 2) + np.power(promy,2))
        errores.append(rad)

        totales.append(len(dentrox))

        plt.figure()
        plt.scatter(dentrox,dentroy,label='Geolocalizaciones aleatorias', s=50)
        plt.scatter(circlex,circley, s=10)
        plt.scatter(promx,promy,label='Promedio',color='red', s=50)
        plt.xlabel('Longitud normalizada' , fontsize = 20)
        plt.ylabel('Latitud normalizada', fontsize = 20)
        plt.title(str(len(dentrox))+' reportes', fontsize = 30)
        plt.legend(fontsize = 10)
        plt.savefig(str(len(dentrox))+'.png')
        #plt.show()

    plt.figure()
    plt.plot(totales,errores,label='Distancia al centro del promedio de posiciones', linewidth=7.0)
    plt.xlabel('N' , fontsize = 20)
    plt.ylabel('Distancia', fontsize = 20)
    plt.title('Error', fontsize = 30)
    plt.legend(fontsize = 10)
    plt.savefig('error.png')
    #plt.show()


4.6154704,-74.0684662
4.7497758,-74.0948111

N_cobre=70 #200
N_cto = 30 #150
N_externos = 200
N_afiliados = 300

xcobre =[]
ycobre =[]

xcto = []
ycto = []

xexternos =[]
yexternos =[]

xafiliados =[]
yafiliados =[]



























#print (GL_to_dir(4.11557833,-73.6230763))
#print (GL_to_dir(4.43702,-75.21407))
#print (GL_to_dir(4.451442,-75.190438))
#print ( dir_to_GL("Calle 3 Sur # 30B-03", "Meta", "Villavicencio"))
