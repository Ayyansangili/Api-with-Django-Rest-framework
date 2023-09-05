from django.db import connection
from .models import CollectionQuery
from rest_framework.exceptions import APIException





def exec_raw_sql(qry_key, qry_vars=dict()):
    try:
        coll_qry = CollectionQuery.objects.filter(key=qry_key).first()
        
        if coll_qry is not None:
            replaced_query = replace_query(coll_qry.query, qry_vars)
            #print(replaced_query)
           
            cursor = connection.cursor()
            cursor.execute(replaced_query)
            #print(cursor)
            #cursor.execute("select * from adm_fileupload where tmp_file_name = 'storage/tmp/OdoQxBNoFmFo_bootstrapnavbar.txt' ")

            res_vals = dict_fetch_all(cursor)
            cursor.close()
            
            return res_vals
        else:
            raise TypeError('Unable to find option key.')

    except Exception as e:
        raise APIException(e)


def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]
    
    
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
        ]

def replace_query(qry, qry_vars):
    replquery = qry
    #qry_vars = {"id" : "1"}
    for key in qry_vars:
        replquery = replquery.replace("@_" + key, str(qry_vars[key]))
        
        
        #select * from adm_roles where id = @_id ;
        #select * from adm_roles where id = 1 
        #replquery = replquery + str(" ") + str("where") + str(" ")+ str(key) + str(" " )+str("=") +str(" ") + str(qry_vars[key])
    #print(replquery)
    return replquery 