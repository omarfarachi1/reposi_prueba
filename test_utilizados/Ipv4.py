class ValidarDireccionesIp:

    def ValidarIpTrue(self, ip):
        if self.ValidarIp(ip):
            return True

    def ValidarIpFalse(self, ip):
        if self.ValidarIp(ip):
            return False

    def ValidarIp(self, ip):
        separador = ip.split('.')
        if len(separador) != 4:
            return False

        for i in separador:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
