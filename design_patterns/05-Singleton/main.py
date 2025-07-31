from singleton import Singleton

def main():
  print("=== Testing Basic Singleton ===")
  
  print("Start.")
  
  obj1 = Singleton.get_instance(100)
  obj2 = Singleton.get_instance(200) # 200 is ignored
  obj3 = Singleton(300) # 300 is ignored
  
  if obj1 is obj2 is obj3:
    print("obj1, obj2, obj3 are the same instances.")
  else:
    print("obj1, obj2, obj3 are not the same instances.")
  
  print(f"obj1 id: {id(obj1)} {obj1.value}") # 100
  print(f"obj2 id: {id(obj2)} {obj2.value}")
  print(f"obj3 id: {id(obj3)} {obj3.value}")
  
  print(f"Business method: {obj1.some_business_method()}")
  
  print("End.\n")

if __name__ == "__main__":
  main()
