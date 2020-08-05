import cx_Oracle,time,datetime,folium
from datetime import datetime as dt
import pandas

def count_faulty():
    conn=cx_Oracle.connect('<__connection__>')
    cur=conn.cursor()
    query = "select count(unique DN) from fx_alarm where Text like '%CELL FAULTY%' and CANCEL_TIME is null"
    cur.execute(query)
    faulty_count = cur.fetchall()
    cur.close()
    conn.close()
    return faulty_count

def faulty_live():
    conn=cx_Oracle.connect('<__connection__>')
    cur=conn.cursor()
    print("hi")
    query = "select unique DN from fx_alarm where Text like '%CELL FAULTY%' and CANCEL_TIME is null"
    cur.execute(query)
    faulty_live_list = cur.fetchall()
    cur.close()
    conn.close()
    print(type(faulty_live_list[0][0]))
    return faulty_live_list

def cord_link_lat(dn_short):
    names=['FDD_E-NodeB','LAT','LONG']
    cord_book=pandas.read_excel("Book1.xls",header=None,names=names)
    book_dn = list(cord_book['FDD_E-NodeB'])
    book_lat = list(cord_book["LAT"])
    book_long = list(cord_book["LONG"])
    for (j,test_single) in enumerate(book_dn):
        if (str(dn_short)) == (str(test_single)):
            import math
            if math.isnan(book_lat[j]):
                pass
            elif math.isnan(book_long[j]):
                pass
            else:
                return str(book_lat[j])
                break #breakhere

def cord_link_long(dn_short):
    names=['FDD_E-NodeB','LAT','LONG']
    cord_book=pandas.read_excel("Book1.xls",header=None,names=names)
    book_dn = list(cord_book['FDD_E-NodeB'])
    book_lat = list(cord_book["LAT"])
    book_long = list(cord_book["LONG"])
    for (j,test_single) in enumerate(book_dn):
        if (str(dn_short)) == (str(test_single)):
            import math
            if math.isnan(book_lat[j]):
                pass
            elif math.isnan(book_long[j]):
                pass
            else:
                print(book_lat[j])
                return str(book_long[j])
                break #breakhere

def shrink_dn (faulty_live_list):
    # df_faulty= pandas.DataFrame.from_records(faulty_live_list)
    dn=faulty_live_list
    DN_small = pandas.Series([])
    Long = pandas.Series(['0'])
    Lat = pandas.Series(['0'])
    for (j,dn_single) in enumerate(dn):
        dn_short=""
        for (i,dn_single_alpha) in enumerate(dn_single[0]):
            if dn_single_alpha.isdigit():
                dn_short = dn_short + dn_single_alpha
            if i==21:
                break #breakhere
        DN_small [j] = dn_short
        b=cord_link_lat(str(dn_short))
        a=cord_link_long(str(dn_short))

        Lat[j]=b
        Long[j]=a
    df_faulty = pandas.DataFrame(list(zip(DN_small, Long,Lat)),columns =['DN', 'LONG','LAT'])
    return df_faulty

def plot_on_map(df_faulty):
    map_dn=list(df_faulty["DN"])
    map_lat=list(df_faulty["LAT"])
    map_long=list(df_faulty["LONG"])
    map = folium.Map(location=[18.2340,78.703],zoom_start=8, titles="Stamen")
    fg_node=folium.FeatureGroup(name="Node")
    #fgpop=folium.FeatureGroup(name="Population")
    for lt,ln,dn in zip(map_lat,map_long,map_dn):
        if lt is not None:
            if ln is not None:
                icon = folium.features.CustomIcon('tower.png',icon_size=(50, 50))
                print(lt)
                fg_node.add_child(folium.Marker(location=[float(str(lt)),float(str(ln))],radius=6,popup=str(dn)+"m", color = 'grey',fill_opacity=0.7,icon=icon))
    map.add_child(fg_node)
    map.add_child(folium.LayerControl())
    map.save("new.html")

def supp_info_pci(name):
    conn=cx_Oracle.connect('<__connection__>')
    cur=conn.cursor()
    query = "select * from fx_alarm where SUPPLEMENTARY_INFO like '%PCI%' "
    cur.execute(query)
    pci = cur.fetchall()
    pci_export = pandas.DataFrame.from_records(pci)
    date=str(dt.now().year) + '-' + str(dt.now().month) + '-' + str(dt.now().day)
    export_name= 'export'+ date + '.xlsx'
    pci_export.to_excel(export_name,encoding="utf-8")
    cur.close()
    conn.close()

def all_now(date):
    conn=cx_Oracle.connect('<__connection__>')
    cur=conn.cursor()
    query=" Select dn,SEVERITY ,text,alarm_number,to_char(alarm_time,'yyyy-mm-dd
    hh24:mi')\
    Alarm_time,to_char(cancel_time,'yyyy-mm-dd hh24:mi') Cancel_time, SUPPLEMENTARY_INFO from \
    fx_alarm where to_char(Alarm_TIME,'yyyy-mm-dd')='"+ date+"' and alarm_number in \
    ('61611','3721','61084','61058','61059','61623','7108','3379','70394','70399','3159','7107','7657') "
    cur.execute(query)
    all = cur.fetchall()
    all_export = pandas.DataFrame.from_records(all)
    date=str(dt.now().year) + '-' + str(dt.now().month) + '-' + str(dt.now().day)
    export_name= 'export'+ date + '.xlsx'
    all_export.to_excel(export_name,encoding="utf-8")
    cur.close()
    conn.close()
