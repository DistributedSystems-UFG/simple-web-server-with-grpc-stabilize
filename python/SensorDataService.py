from concurrent import futures
import logging

import grpc
import SensorDataService_pb2
import SensorDataService_pb2_grpc

sensorDB=[]

class SensorDataServer(SensorDataService_pb2_grpc.SensorDataServiceServicer):

  def CreateSensorData(self, request, context):
    data = {
    'id':request.id,
    'date':request.date,
    'location':request.location,
    'temperature':request.temperature
    }
    sensorDB.append(data)
    return SensorDataService_pb2.StatusReply(status='OK')

  def GetSensorDataFromId(self, request, context):
    usr = [ sensor for sensor in sensorDB if (sensor['id'] == request.id) ] 
    return SensorDataService_pb2.SensorData(id=usr[0]['id'], date=usr[0]['date'], location=usr[0]['location'], temperature=usr[0]['temperature'])

  def GetSensorDataFromDate(self, request, context):
    data = [ sensor for sensor in sensorDB if (sensor['date'] == request.date) ] 
    list = SensorDataService_pb2.SensorDataList()
    for item in data:
      sensor_data = SensorDataService_pb2.SensorData(id=item['id'], date=item['date'], location=item['location'], temperature=item['temperature']) 
      list.sensor_data.append(sensor_data)
    return list
    
  def GetSensorDataFromLocation(self, request, context):
    data = [ sensor for sensor in sensorDB if (sensor['location'] == request.location) ] 
    list = SensorDataService_pb2.SensorDataList()
    for item in data:
      sensor_data = SensorDataService_pb2.SensorData(id=item['id'], date=item['date'], location=item['location'], temperature=item['temperature']) 
      list.sensor_data.append(sensor_data)
    return list

  def ListAllSensorData(self, request, context):
    list = SensorDataService_pb2.SensorDataList()
    for item in sensorDB:
      sensor_data = SensorDataService_pb2.SensorData(id=item['id'], date=item['date'], location=item['location'], temperature=item['temperature']) 
      list.sensor_data.append(sensor_data)
    return list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SensorDataService_pb2_grpc.add_SensorDataServiceServicer_to_server(SensorDataServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()