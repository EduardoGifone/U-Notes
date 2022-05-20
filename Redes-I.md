# REDES DE COMPUTADORAS I

***

## 19 mayo - introductorio

#### Tipos de redes
* Redes cableadas
* Redes inalambricas

#### IP (Protocolo de internet)
* IP Privada (casa)
* IP Publica (internet)
* 192.168.0.1

    | red | | | host |
    | - | - | - | - |
    | 192 | 168| 0 | 1 |

#### Tipos de redes IPv4

| Tipo red | --- | --- | --- | --- | total host |
| --- | --- | --- | --- | --- | --- |
| A | red | host | host | host | *2^24* |
| B | red | red | host | host | *2^16* |
| C | red | red | red | host | *2^8* |

* Direcciones especiales

| red | host | host | host | |
| - | - | - | - | - |
| 14 | 0 | 0 | 0 | **ID** |
| 14 | 255 | 255 | 255 | **Broadcast** |

* A 
    * *0 1 1 1 1 1 1 1.\_.\_\._*

    | red | host | host | host |
    | - | - | - | - |
    | 0 | _ | _ | _ |
    | 127 | _ | _ | _ |

* B 
    * *1 0 _ _ _ _ _ _ .\_ .\_ .\_*

    | red | red | host | host |
    | - | - | - | - |
    | 128 | 0 | _ | _ |
    | 191 | 255 | _ | _ |

* C 
    * *1 1 0 _ _ _ _ _ .\_ .\_ .\_*

    | red | red | red | host |
    | - | - | - | - |
    | 192 | 0 | 0 | _ |
    | 223 | 255 | 255 | _ |

* **Redes de prueba**
    * D 
        * *1 1 1 0 _ _ _ _ .\_ .\_ .\_*

        | red | red | red | host |
        | - | - | - | - |
        | 224 | 0 | 0 | _ |
        | 239 | 255 | 255 | _ |

    * E 
        * *1 1 1 1 _ _ _ _ .\_ .\_ .\_*

        | red | red | red | host |
        | - | - | - | - |
        | 240 | 0 | 0 | _ |
        | 255 | 255 | 255 | _ |

#### Mascara de red

| Tipo red | - | - | - | - | ICDR |
| - | - | - | - | - | - |
| A | 255 | 0 | 0 | 0 | /8 |
| B | 255 | 255 | 0 | 0 | /16 |
| C | 255 | 255 | 255 | 0 | /24 |

* Para hallar el ID de la red se hace una operacion ***and***
    * **IP** *and* **MASCARA** = ***ID***

*** 

## 20 mayo - Usando Packet Tracer

#### Cable de red
* UTP 
* Tiene categorias
* Maximo 90 metros
* Disposicion de cables
    * Cruzado para mismo equipos
    * No cruzado para diferentes equipos
![Normas](https://image.jimcdn.com/app/cms/image/transf/dimension=259x10000:format=png/path/s8c0b436340bfa088/image/i88812c7dcd75a617/version/1561941775/image.png)
