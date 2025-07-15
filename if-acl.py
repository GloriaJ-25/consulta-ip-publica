aclNum = int(input("Cual es el numero ACL IPv4?"))

if aclNum >= 1 and aclNum <= 99:
    print("Esta es una ACL IPv4 estandar.")

elif aclNum >= 100 and aclNum <= 199:
    print("Esta es una ACL IPv4 estendida.")

else:
    print("Esta ACL IPv4 no es estandar ni extendida.")