from __future__ import print_function
import logging

import grpc
import SensorDataService_pb2
import SensorDataService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = SensorDataService_pb2_grpc.SensorDataServiceStub(channel)

        # Query an sensor data
        response = stub.GetSensorDataFromId(SensorDataService_pb2.SensorId(id=1))
        print ('Sensor\'s data (id= 1): ' + str(response))
        
        # List all sensor data for a given date
        response = stub.GetSensorDataFromDate(SensorDataService_pb2.SensorDate(date='10-12-2022 21:00:00'))
        print ('Sensor\'s data (date= 10-12-2022): ' + str(response))
        
        # List all sensor data for a given location
        response = stub.GetSensorDataFromLocation(SensorDataService_pb2.SensorLocation(location='Goiânia'))
        print ('Sensor\'s data (location= Goiânia): ' + str(response))
        
        # List all sensor data for a given location
        response = stub.GetSensorDataFromLocation(SensorDataService_pb2.SensorLocation(location='Manaus'))
        print ('Sensor\'s data (location= Manaus): ' + str(response))

        # List all sensor data
        response = stub.ListAllSensorData(SensorDataService_pb2.EmptyMessage())
        print ('All sensor data: ' + str(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()