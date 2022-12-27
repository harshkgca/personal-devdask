# from dask_cloudprovider.gcp import GCPCluster
# import dask.config
# from google.oauth2.service_account import Credentials
# import os
# from dask.distributed import Client
# import dask.array as da
#
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'retailigence2020.json'
# creds = Credentials.from_service_account_file("retailigence2020.json")
# print(creds.project_id)
# dask.config.set({"cloudprovider.gcp.projectid": creds.project_id})
# cluster = GCPCluster(
#     n_workers=1,
#     # network='retail2020-network',
#     # network_projectid=creds.project_id,
#     projectid=creds.project_id,
#     zone='europe-west3-a',
#     auto_shutdown=False,
#     # auto_shutdown=True,
#     # docker_image="eu.gcr.io/retailigence-2020/dev-daskgateway@sha256:27145b402b608dd15e3495e2fadad6c171dbaa4cbd7b377ac8a07bc9041917bc",
#     docker_image="eu.gcr.io/retailigence-2020/dev-daskgateway:2.755",
#     # machine_type="n1-custom-4-32768")
#     # machine_type="custom-6-32768")
#     machine_type="n1-standard-1")
# print('cluster created')
# client = Client(cluster)
# print(client)
# arr = da.random.random((1000, 1000), chunks=(100, 100))
# print(arr)
# arr.mean().compute()
# print('computed')
# cluster.close()

''''''
import time

from dask_cloudprovider.gcp import GCPCluster
import os
from dask.distributed import Client
import dask.array as da

from pymongo import MongoClient
mongo = 'mongodb://HEB_Admin:H38na0dm1n3yMgphb18rj@34.162.41.6:27017/DEV_HEB_DB'
mongo_uri = MongoClient(mongo)
print(mongo_uri)
# exit(0)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'retailigence2020.json'
# cloud_init = GCPCluster.get_cloud_init(
#         security=True,
#         docker_args="--privileged",
#         extra_bootstrap=["gcloud auth print-access-token"],
#     )
# exit()
# cloud_init = GCPCluster.get_cloud_init(
#         security=True,
#         docker_args="--privileged",
#         extra_bootstrap=["gcloud auth print-access-token"],
#         # docker_image="asia.gcr.io/retailigence-2020/dev-daskgateway:2.764",
#         docker_image="asia.gcr.io/retailigence-2020/dev-daskgateway:2.765",
#     )
# cld = GCPCluster.get_cloud_init()
# print(cloud_init)
# exit()
cluster = GCPCluster(n_workers=1,
                     projectid='retailigence-2020',
                     # docker_image="eu.gcr.io/retailigence-2020/dev-daskgateway:2.761",
                     # docker_image="eu.gcr.io/retailigence-2020/dev-daskgateway@sha256:c934df9c52bf7eebb05edd617ebe7cb5228753d3750d96083d9ca3fd4e5b58bc",
                     # docker_image="retailigence-2020/dev-daskgateway:2.761",
                     # docker_image="retailigence-2020/dev-daskgateway:2.764",
                     # docker_image="eu.gcr.io/retailigence-2020/dev-daskgateway:2.764",
                     # docker_image="asia.gcr.io/retailigence-2020/dev-daskgateway@sha256:4350e58f11e00867d720b8992fc2580689fe32619f444ab9625e0079c9cd5bc3",
                     # docker_image="asia.gcr.io/retailigence-2020/dev-daskgateway:2.764",
                     # docker_image="asia.gcr.io/retailigence-2020/dev-daskgateway:2.774",
                     docker_image="asia.gcr.io/retailigence-2020/dev-daskgateway:2.775",
                     # network='subnet4',
                     docker_args='',
                     # docker_args="sudo docker pull asia.gcr.io/retailigence-2020/dev-daskgateway:2.773 \n ",
                     zone='europe-west3-a',
                     auto_shutdown=False,
                     # machine_type="n1-custom-6-32768"
                     )


def test():
    try:
        from pymongo import MongoClient
        mongo = os.environ['mongo_uri']
        mongo_uri = MongoClient(mongo)

        print(os.environ['mongo_uri'])
        ''''''
        # dir_list = os.listdir('/')
        # dir_list1 = os.listdir('/etc')
        # dir_list2 = os.listdir('/usr')
        # dir_list3 = os.listdir('/usr/bin')
        # dir_list4 = os.listdir('.')
        # with open('/usr/bin/prepare.sh', 'r') as file:
        #     data = file.read().rstrip()
        #
        # with open('.dockerenv', 'r') as file:
        #     data1 = file.read().rstrip()
        #
        # # path = 'Dockerfile'
        # # print(os.path.basename(path))
        # # filePath = os.path.basename(path)
        # filePath = ''
        #
        # # import os
        # file_ = 'Dockerfile'
        #
        # for root, dirs, files in os.walk('/'):
        #     for name in files:
        #         if file_ in name:
        #             print(os.path.abspath(os.path.join(root, name)))
        #             filePath = os.path.abspath(os.path.join(root, name))
        ''''''

        # mongo_db = mongo_uri['DEV_HEB_DB']
        # mongo_db.test.insert_one({"dask func": True})
        # arr = da.random.random((1000, 1000), chunks=(100, 100))
        # print(arr)
        # val = arr.mean().compute()
        # print(val)
        print('computed')
        return {
            'monogo':os.environ['mongo_uri'],
            # 'path':dir_list,
            # 'path1':dir_list1,
            # 'path2':dir_list2,
            # 'path3':dir_list3,
            # 'path4':dir_list4,
            # 'data':data,
            # 'data1':data1,
            # 'filePath': filePath,
            'mongo':mongo,
            'mongo_connect':mongo_uri
        }
        # return True
    except Exception as e:
        print(e)
        return e

print('cluster created')
client = Client(cluster)
print(client)
print(client.dashboard_link)
''''''
# arr = da.random.random((1000, 1000), chunks=(100, 100))
# print(arr)
# val = arr.mean().compute()
# print(val)
# print('computed')
''''''
a = client.submit(test)
data = client.gather(a)
print(data)
# client.gather(a)
stat = None
while (stat == None) or (stat == 'pending'):
    # from pymongo import MongoClient
    # print(os.environ['mongo_uri'])
    # mongo_uri = MongoClient('mongodb://HEB_Admin:H38na0dm1n3yMgphb18rj@192.168.0.24:27017/DEV_HEB_DB')
    # mongo_db = mongo_uri['DEV_HEB_DB']
    stat = a.status
    print(a.status)
    # data = a.result()
    print('100')
    time.sleep(10)
print(stat)
# data = client.gather(a)
''''''
print(data)
print('************************************')
# print(data['path'])
# print(data['path1'])
# print(data['path2'])
# print(data['path3'])
# print(data['path4'])
# print('************************************')
# print(data['data'])
# print('************************************')
# print(data['data1'])
# print('************************************')
# print(data['filePath'])
# print('************************************')
# print(data['mongo_connect'])
# print('************************************')
client.close()
cluster.close()
