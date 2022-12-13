from __future__ import print_function
import logging

import grpc
import SensorDataService_pb2
import SensorDataService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = SensorDataService_pb2_grpc.SensorDataServiceStub(channel)

        # Add new sensor datas
        response = stub.CreateSensorData(SensorDataService_pb2.SensorData(id=1, date='12-12-2022 21:00:00', location='São Paulo', temperature='29'))
        print ('Added new sensor data ' + response.status)
        response = stub.CreateSensorData(SensorDataService_pb2.SensorData(id=2, date='11-12-2022 21:00:00', location='Manaus', temperature='31'))
        print ('Added new sensor data ' + response.status)
        response = stub.CreateSensorData(SensorDataService_pb2.SensorData(id=3, date='10-12-2022 21:00:00', location='Goiânia', temperature='26'))
        print ('Added new sensor data ' + response.status)
        response = stub.CreateSensorData(SensorDataService_pb2.SensorData(id=4, date='10-12-2022 21:00:00', location='Goiânia', temperature='18'))
        print ('Added new sensor data ' + response.status)
        response = stub.CreateSensorData(SensorDataService_pb2.SensorData(id=5, date='20-12-2022 12:00:00', location='Manaus', temperature='20'))
        print ('Added new sensor data ' + response.status)

if __name__ == '__main__':
    logging.basicConfig()
    run()