from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/positions")
def get_endpoints():
    endpoints_list = [
  {
    "ultimo": "0 Día(s) 0 hora(s) 2 minuto(s) ",
    "imei": "354890871456789",
    "movil_id": "1880045678",
    "fecha": "2025-06-02",
    "hora": "08:15",
    "lat": "20.52353000",
    "lng": "-103.31127000",
    "latshort": "20.5235",
    "lonshort": "-103.3112",
    "economico": "JAL-001",
    "crs": "45.30",
    "bateria": "13.85 v",
    "placas": "GDL-001A",
    "spd": "35 Km/h",
    "spd1": 35,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "58",
    "ubi": "Av. Vallarta 1234, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "205235",
    "lonshort2": "103311",
    "fecha_equipo": "02/06/2025 08:15:23",
    "temp1": "22.5",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "45623"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 0 minuto(s) ",
    "imei": "354890871456790",
    "movil_id": "1880045679",
    "fecha": "2025-06-02",
    "hora": "08:17",
    "lat": "20.53421000",
    "lng": "-103.29845000",
    "latshort": "20.5342",
    "lonshort": "-103.2984",
    "economico": "JAL-001",
    "crs": "52.10",
    "bateria": "13.90 v",
    "placas": "GDL-001A",
    "spd": "42 Km/h",
    "spd1": 42,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "61",
    "ubi": "Calz. Lázaro Cárdenas 567, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "205342",
    "lonshort2": "103298",
    "fecha_equipo": "02/06/2025 08:17:45",
    "temp1": "23.1",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "45625"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456791",
    "movil_id": "1880045680",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "20.54789000",
    "lng": "-103.27234000",
    "latshort": "20.5478",
    "lonshort": "-103.2723",
    "economico": "JAL-001",
    "crs": "78.45",
    "bateria": "13.75 v",
    "placas": "GDL-001A",
    "spd": "28 Km/h",
    "spd1": 28,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "55",
    "ubi": "Av. Américas 890, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "205478",
    "lonshort2": "103272",
    "fecha_equipo": "02/06/2025 08:16:12",
    "temp1": "24.2",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "45627"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 3 minuto(s) ",
    "imei": "354890871456792",
    "movil_id": "1880045681",
    "fecha": "2025-06-02",
    "hora": "08:14",
    "lat": "20.51234000",
    "lng": "-103.33456000",
    "latshort": "20.5123",
    "lonshort": "-103.3345",
    "economico": "JAL-001",
    "crs": "0.00",
    "bateria": "12.45 v",
    "placas": "GDL-001A",
    "spd": "0 km/h",
    "spd1": 0,
    "in_state": "00000000",
    "fix": "1",
    "signal_strength": "48",
    "ubi": "C. Morelos 123, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD DETENIDA",
    "latshort2": "205123",
    "lonshort2": "103334",
    "fecha_equipo": "02/06/2025 08:14:33",
    "temp1": "21.8",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "45629"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 0 minuto(s) ",
    "imei": "354890871456793",
    "movil_id": "1880045682",
    "fecha": "2025-06-02",
    "hora": "08:17",
    "lat": "20.49876000",
    "lng": "-103.35234000",
    "latshort": "20.4987",
    "lonshort": "-103.3523",
    "economico": "JAL-001",
    "crs": "125.67",
    "bateria": "14.12 v",
    "placas": "GDL-001A",
    "spd": "55 Km/h",
    "spd1": 55,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "62",
    "ubi": "Periférico Norte 2345, Zapopan, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "204987",
    "lonshort2": "103352",
    "fecha_equipo": "02/06/2025 08:17:56",
    "temp1": "25.3",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "45631"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 2 minuto(s) ",
    "imei": "354890871456794",
    "movil_id": "1880045683",
    "fecha": "2025-06-02",
    "hora": "08:15",
    "lat": "20.48234000",
    "lng": "-103.38765000",
    "latshort": "20.4823",
    "lonshort": "-103.3876",
    "economico": "JAL-001",
    "crs": "89.23",
    "bateria": "13.67 v",
    "placas": "GDL-001A",
    "spd": "38 Km/h",
    "spd1": 38,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "57",
    "ubi": "Av. Patria 678, Zapopan, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "204823",
    "lonshort2": "103387",
    "fecha_equipo": "02/06/2025 08:15:41",
    "temp1": "23.7",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "45633"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 4 minuto(s) ",
    "imei": "354890871456795",
    "movil_id": "1880045684",
    "fecha": "2025-06-02",
    "hora": "08:13",
    "lat": "20.46789000",
    "lng": "-103.41234000",
    "latshort": "20.4678",
    "lonshort": "-103.4123",
    "economico": "JAL-001",
    "crs": "156.78",
    "bateria": "13.22 v",
    "placas": "GDL-001A",
    "spd": "22 Km/h",
    "spd1": 22,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "52",
    "ubi": "Av. López Mateos Sur 345, Tlaquepaque, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "204678",
    "lonshort2": "103412",
    "fecha_equipo": "02/06/2025 08:13:18",
    "temp1": "26.1",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "45635"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456796",
    "movil_id": "1880045685",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "19.24056000",
    "lng": "-103.72478000",
    "latshort": "19.2405",
    "lonshort": "-103.7247",
    "economico": "COL-002",
    "crs": "234.12",
    "bateria": "12.98 v",
    "placas": "COL-002B",
    "spd": "45 Km/h",
    "spd1": 45,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "59",
    "ubi": "Av. Universidad 123, Colima, Colima, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "192405",
    "lonshort2": "103724",
    "fecha_equipo": "02/06/2025 08:16:27",
    "temp1": "28.4",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "67891"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 0 minuto(s) ",
    "imei": "354890871456797",
    "movil_id": "1880045686",
    "fecha": "2025-06-02",
    "hora": "08:17",
    "lat": "19.25234000",
    "lng": "-103.71234000",
    "latshort": "19.2523",
    "lonshort": "-103.7123",
    "economico": "COL-002",
    "crs": "0.00",
    "bateria": "13.45 v",
    "placas": "COL-002B",
    "spd": "0 km/h",
    "spd1": 0,
    "in_state": "00000000",
    "fix": "1",
    "signal_strength": "64",
    "ubi": "C. Constitución 456, Colima, Colima, Mexico",
    "title": "UNIDAD DETENIDA",
    "latshort2": "192523",
    "lonshort2": "103712",
    "fecha_equipo": "02/06/2025 08:17:52",
    "temp1": "29.2",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "67893"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 3 minuto(s) ",
    "imei": "354890871456798",
    "movil_id": "1880045687",
    "fecha": "2025-06-02",
    "hora": "08:14",
    "lat": "19.22876000",
    "lng": "-103.74567000",
    "latshort": "19.2287",
    "lonshort": "-103.7456",
    "economico": "COL-002",
    "crs": "67.89",
    "bateria": "14.03 v",
    "placas": "COL-002B",
    "spd": "32 Km/h",
    "spd1": 32,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "56",
    "ubi": "Blvd. Camino Real 789, Colima, Colima, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "192287",
    "lonshort2": "103745",
    "fecha_equipo": "02/06/2025 08:14:08",
    "temp1": "27.8",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "67895"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456799",
    "movil_id": "1880045688",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "21.88123000",
    "lng": "-102.29456000",
    "latshort": "21.8812",
    "lonshort": "-102.2945",
    "economico": "AGS-003",
    "crs": "145.67",
    "bateria": "13.78 v",
    "placas": "AGS-003C",
    "spd": "48 Km/h",
    "spd1": 48,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "61",
    "ubi": "Av. Aguascalientes Sur 234, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "218812",
    "lonshort2": "102294",
    "fecha_equipo": "02/06/2025 08:16:34",
    "temp1": "24.6",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "89234"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 2 minuto(s) ",
    "imei": "354890871456800",
    "movil_id": "1880045689",
    "fecha": "2025-06-02",
    "hora": "08:15",
    "lat": "21.89567000",
    "lng": "-102.27890000",
    "latshort": "21.8956",
    "lonshort": "-102.2789",
    "economico": "AGS-003",
    "crs": "89.34",
    "bateria": "12.67 v",
    "placas": "AGS-003C",
    "spd": "25 Km/h",
    "spd1": 25,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "53",
    "ubi": "C. Madero 567, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "218956",
    "lonshort2": "102278",
    "fecha_equipo": "02/06/2025 08:15:19",
    "temp1": "23.9",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "89236"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 0 minuto(s) ",
    "imei": "354890871456801",
    "movil_id": "1880045690",
    "fecha": "2025-06-02",
    "hora": "08:17",
    "lat": "21.91234000",
    "lng": "-102.25678000",
    "latshort": "21.9123",
    "lonshort": "-102.2567",
    "economico": "AGS-003",
    "crs": "0.00",
    "bateria": "13.89 v",
    "placas": "AGS-003C",
    "spd": "0 km/h",
    "spd1": 0,
    "in_state": "00000000",
    "fix": "1",
    "signal_strength": "67",
    "ubi": "Plaza de Armas 890, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD DETENIDA",
    "latshort2": "219123",
    "lonshort2": "102256",
    "fecha_equipo": "02/06/2025 08:17:44",
    "temp1": "25.7",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "89238"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 5 minuto(s) ",
    "imei": "354890871456802",
    "movil_id": "1880045691",
    "fecha": "2025-06-02",
    "hora": "08:12",
    "lat": "20.67234000",
    "lng": "-103.34567000",
    "latshort": "20.6723",
    "lonshort": "-103.3456",
    "economico": "JAL-004",
    "crs": "276.45",
    "bateria": "11.98 v",
    "placas": "GDL-004D",
    "spd": "62 Km/h",
    "spd1": 62,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "45",
    "ubi": "Carretera a Chapala Km 15, Tlajomulco, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "206723",
    "lonshort2": "103345",
    "fecha_equipo": "02/06/2025 08:12:56",
    "temp1": "22.3",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "123456"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 3 minuto(s) ",
    "imei": "354890871456803",
    "movil_id": "1880045692",
    "fecha": "2025-06-02",
    "hora": "08:14",
    "lat": "20.68901000",
    "lng": "-103.32145000",
    "latshort": "20.6890",
    "lonshort": "-103.3214",
    "economico": "JAL-004",
    "crs": "156.78",
    "bateria": "12.34 v",
    "placas": "GDL-004D",
    "spd": "41 Km/h",
    "spd1": 41,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "58",
    "ubi": "Av. Niños Héroes 345, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "206890",
    "lonshort2": "103321",
    "fecha_equipo": "02/06/2025 08:14:21",
    "temp1": "24.8",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "123458"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456804",
    "movil_id": "1880045693",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "19.18456000",
    "lng": "-103.78234000",
    "latshort": "19.1845",
    "lonshort": "-103.7823",
    "economico": "COL-005",
    "crs": "67.12",
    "bateria": "13.56 v",
    "placas": "COL-005E",
    "spd": "38 Km/h",
    "spd1": 38,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "62",
    "ubi": "Carr. Colima-Villa de Álvarez Km 5, Villa de Álvarez, Col., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "191845",
    "lonshort2": "103782",
    "fecha_equipo": "02/06/2025 08:16:47",
    "temp1": "30.1",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "78945"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 4 minuto(s) ",
    "imei": "354890871456805",
    "movil_id": "1880045694",
    "fecha": "2025-06-02",
    "hora": "08:13",
    "lat": "19.17234000",
    "lng": "-103.81567000",
    "latshort": "19.1723",
    "lonshort": "-103.8156",
    "economico": "COL-005",
    "crs": "0.00",
    "bateria": "12.89 v",
    "placas": "COL-005E",
    "spd": "0 km/h",
    "spd1": 0,
    "in_state": "00000000",
    "fix": "1",
    "signal_strength": "49",
    "ubi": "Centro Comercial Plaza Crystal, Villa de Álvarez, Col., Mexico",
    "title": "UNIDAD DETENIDA",
    "latshort2": "191723",
    "lonshort2": "103815",
    "fecha_equipo": "02/06/2025 08:13:38",
    "temp1": "28.9",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "78947"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 2 minuto(s) ",
    "imei": "354890871456806",
    "movil_id": "1880045695",
    "fecha": "2025-06-02",
    "hora": "08:15",
    "lat": "21.93567000",
    "lng": "-102.23145000",
    "latshort": "21.9356",
    "lonshort": "-102.2314",
    "economico": "AGS-006",
    "crs": "298.67",
    "bateria": "14.15 v",
    "placas": "AGS-006F",
    "spd": "53 Km/h",
    "spd1": 53,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "65",
    "ubi": "Blvd. Zacatecas Norte 678, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "219356",
    "lonshort2": "102231",
    "fecha_equipo": "02/06/2025 08:15:29",
    "temp1": "26.4",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "156789"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 0 minuto(s) ",
    "imei": "354890871456807",
    "movil_id": "1880045696",
    "fecha": "2025-06-02",
    "hora": "08:17",
    "lat": "21.95123000",
    "lng": "-102.20987000",
    "latshort": "21.9512",
    "lonshort": "-102.2098",
    "economico": "AGS-006",
    "crs": "123.45",
    "bateria": "13.42 v",
    "placas": "AGS-006F",
    "spd": "29 Km/h",
    "spd1": 29,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "59",
    "ubi": "Av. Universidad 234, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "219512",
    "lonshort2": "102209",
    "fecha_equipo": "02/06/2025 08:17:13",
    "temp1": "25.1",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "156791"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 3 minuto(s) ",
    "imei": "354890871456808",
    "movil_id": "1880045697",
    "fecha": "2025-06-02",
    "hora": "08:14",
    "lat": "20.58934000",
    "lng": "-103.26789000",
    "latshort": "20.5893",
    "lonshort": "-103.2678",
    "economico": "JAL-007",
    "crs": "234.89",
    "bateria": "12.78 v",
    "placas": "GDL-007G",
    "spd": "47 Km/h",
    "spd1": 47,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "54",
    "ubi": "Av. Chapultepec Norte 567, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "205893",
    "lonshort2": "103267",
    "fecha_equipo": "02/06/2025 08:14:55",
    "temp1": "23.5",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "234567"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456809",
    "movil_id": "1880045698",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "20.60234000",
    "lng": "-103.24156000",
    "latshort": "20.6023",
    "lonshort": "-103.2415",
    "economico": "JAL-007",
    "crs": "89.23",
    "bateria": "13.91 v",
    "placas": "GDL-007G",
    "spd": "33 Km/h",
    "spd1": 33,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "61",
    "ubi": "Plaza del Sol, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "206023",
    "lonshort2": "103241",
    "fecha_equipo": "02/06/2025 08:16:02",
    "temp1": "24.9",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "234569"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 5 minuto(s) ",
    "imei": "354890871456810",
    "movil_id": "1880045699",
    "fecha": "2025-06-02",
    "hora": "08:12",
    "lat": "19.31245000",
    "lng": "-103.68934000",
    "latshort": "19.3124",
    "lonshort": "-103.6893",
    "economico": "COL-008",
    "crs": "167.34",
    "bateria": "11.89 v",
    "placas": "COL-008H",
    "spd": "44 Km/h",
    "spd1": 44,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "47",
    "ubi": "Autopista Colima-Guadalajara Km 25, Comala, Col., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "193124",
    "lonshort2": "103689",
    "fecha_equipo": "02/06/2025 08:12:41",
    "temp1": "31.2",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "98765"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 2 minuto(s) ",
    "imei": "354890871456811",
    "movil_id": "1880045700",
    "fecha": "2025-06-02",
    "hora": "08:15",
    "lat": "19.32891000",
    "lng": "-103.66234000",
    "latshort": "19.3289",
    "lonshort": "-103.6623",
    "economico": "COL-008",
    "crs": "0.00",
    "bateria": "13.67 v",
    "placas": "COL-008H",
    "spd": "0 km/h",
    "spd1": 0,
    "in_state": "00000000",
    "fix": "1",
    "signal_strength": "52",
    "ubi": "Centro Histórico de Comala, Comala, Col., Mexico",
    "title": "UNIDAD DETENIDA",
    "latshort2": "193289",
    "lonshort2": "103662",
    "fecha_equipo": "02/06/2025 08:15:16",
    "temp1": "29.8",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "98767"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456812",
    "movil_id": "1880045701",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "21.86789000",
    "lng": "-102.31567000",
    "latshort": "21.8678",
    "lonshort": "-102.3156",
    "economico": "AGS-009",
    "crs": "345.67",
    "bateria": "14.08 v",
    "placas": "AGS-009I",
    "spd": "58 Km/h",
    "spd1": 58,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "63",
    "ubi": "Carr. Panamericana Sur Km 8, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "218678",
    "lonshort2": "102315",
    "fecha_equipo": "02/06/2025 08:16:58",
    "temp1": "27.3",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "187654"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 4 minuto(s) ",
    "imei": "354890871456813",
    "movil_id": "1880045702",
    "fecha": "2025-06-02",
    "hora": "08:13",
    "lat": "21.84234000",
    "lng": "-102.34123000",
    "latshort": "21.8423",
    "lonshort": "-102.3412",
    "economico": "AGS-009",
    "crs": "198.45",
    "bateria": "12.56 v",
    "placas": "AGS-009I",
    "spd": "36 Km/h",
    "spd1": 36,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "48",
    "ubi": "Av. Convención de 1914 Norte 890, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "218423",
    "lonshort2": "102341",
    "fecha_equipo": "02/06/2025 08:13:07",
    "temp1": "26.8",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "187656"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 0 minuto(s) ",
    "imei": "354890871456814",
    "movil_id": "1880045703",
    "fecha": "2025-06-02",
    "hora": "08:17",
    "lat": "20.41567000",
    "lng": "-103.45234000",
    "latshort": "20.4156",
    "lonshort": "-103.4523",
    "economico": "JAL-010",
    "crs": "267.89",
    "bateria": "13.73 v",
    "placas": "GDL-010J",
    "spd": "49 Km/h",
    "spd1": 49,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "56",
    "ubi": "Carr. Guadalajara-Chapala Km 18, Tlajomulco, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "204156",
    "lonshort2": "103452",
    "fecha_equipo": "02/06/2025 08:17:31",
    "temp1": "25.6",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "345678"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 3 minuto(s) ",
    "imei": "354890871456815",
    "movil_id": "1880045704",
    "fecha": "2025-06-02",
    "hora": "08:14",
    "lat": "20.39234000",
    "lng": "-103.48901000",
    "latshort": "20.3923",
    "lonshort": "-103.4890",
    "economico": "JAL-010",
    "crs": "89.12",
    "bateria": "12.91 v",
    "placas": "GDL-010J",
    "spd": "27 Km/h",
    "spd1": 27,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "51",
    "ubi": "Av. Santa Margarita 456, Zapopan, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "203923",
    "lonshort2": "103489",
    "fecha_equipo": "02/06/2025 08:14:42",
    "temp1": "24.1",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "345680"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 2 minuto(s) ",
    "imei": "354890871456816",
    "movil_id": "1880045705",
    "fecha": "2025-06-02",
    "hora": "08:15",
    "lat": "19.15678000",
    "lng": "-103.84567000",
    "latshort": "19.1567",
    "lonshort": "-103.8456",
    "economico": "COL-011",
    "crs": "156.78",
    "bateria": "13.84 v",
    "placas": "COL-011K",
    "spd": "41 Km/h",
    "spd1": 41,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "58",
    "ubi": "Blvd. Camino Real de Colima 123, Villa de Álvarez, Col., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "191567",
    "lonshort2": "103845",
    "fecha_equipo": "02/06/2025 08:15:24",
    "temp1": "32.1",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "456789"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456817",
    "movil_id": "1880045706",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "19.13234000",
    "lng": "-103.87891000",
    "latshort": "19.1323",
    "lonshort": "-103.8789",
    "economico": "COL-011",
    "crs": "0.00",
    "bateria": "12.47 v",
    "placas": "COL-011K",
    "spd": "0 km/h",
    "spd1": 0,
    "in_state": "00000000",
    "fix": "1",
    "signal_strength": "44",
    "ubi": "Parque Regional Metropolitano, Villa de Álvarez, Col., Mexico",
    "title": "UNIDAD DETENIDA",
    "latshort2": "191323",
    "lonshort2": "103878",
    "fecha_equipo": "02/06/2025 08:16:39",
    "temp1": "30.7",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "456791"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 4 minuto(s) ",
    "imei": "354890871456818",
    "movil_id": "1880045707",
    "fecha": "2025-06-02",
    "hora": "08:13",
    "lat": "21.97234000",
    "lng": "-102.18567000",
    "latshort": "21.9723",
    "lonshort": "-102.1856",
    "economico": "AGS-012",
    "crs": "278.34",
    "bateria": "13.29 v",
    "placas": "AGS-012L",
    "spd": "52 Km/h",
    "spd1": 52,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "60",
    "ubi": "Carr. a San Luis Potosí Km 12, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "219723",
    "lonshort2": "102185",
    "fecha_equipo": "02/06/2025 08:13:25",
    "temp1": "28.2",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "567890"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 0 minuto(s) ",
    "imei": "354890871456819",
    "movil_id": "1880045708",
    "fecha": "2025-06-02",
    "hora": "08:17",
    "lat": "21.99567000",
    "lng": "-102.15234000",
    "latshort": "21.9956",
    "lonshort": "-102.1523",
    "economico": "AGS-012",
    "crs": "123.56",
    "bateria": "14.21 v",
    "placas": "AGS-012L",
    "spd": "31 Km/h",
    "spd1": 31,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "64",
    "ubi": "Fracc. Pilar Blanco, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "219956",
    "lonshort2": "102152",
    "fecha_equipo": "02/06/2025 08:17:08",
    "temp1": "26.9",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "567892"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 3 minuto(s) ",
    "imei": "354890871456820",
    "movil_id": "1880045709",
    "fecha": "2025-06-02",
    "hora": "08:14",
    "lat": "20.71234000",
    "lng": "-103.28901000",
    "latshort": "20.7123",
    "lonshort": "-103.2890",
    "economico": "JAL-013",
    "crs": "234.78",
    "bateria": "13.05 v",
    "placas": "GDL-013M",
    "spd": "46 Km/h",
    "spd1": 46,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "55",
    "ubi": "Carr. a Nogales Km 22, Guadalajara, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "207123",
    "lonshort2": "103289",
    "fecha_equipo": "02/06/2025 08:14:17",
    "temp1": "23.4",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "678901"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456821",
    "movil_id": "1880045710",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "20.73891000",
    "lng": "-103.25678000",
    "latshort": "20.7389",
    "lonshort": "-103.2567",
    "economico": "JAL-013",
    "crs": "89.45",
    "bateria": "12.83 v",
    "placas": "GDL-013M",
    "spd": "34 Km/h",
    "spd1": 34,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "59",
    "ubi": "Av. Mariano Otero 789, Zapopan, Jalisco, Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "207389",
    "lonshort2": "103256",
    "fecha_equipo": "02/06/2025 08:16:51",
    "temp1": "25.8",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "678903"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 5 minuto(s) ",
    "imei": "354890871456822",
    "movil_id": "1880045711",
    "fecha": "2025-06-02",
    "hora": "08:12",
    "lat": "19.35678000",
    "lng": "-103.62341000",
    "latshort": "19.3567",
    "lonshort": "-103.6234",
    "economico": "COL-014",
    "crs": "167.23",
    "bateria": "11.76 v",
    "placas": "COL-014N",
    "spd": "39 Km/h",
    "spd1": 39,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "46",
    "ubi": "Carr. a Minatitlán Km 8, Comala, Col., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "193567",
    "lonshort2": "103623",
    "fecha_equipo": "02/06/2025 08:12:34",
    "temp1": "33.2",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "789012"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 2 minuto(s) ",
    "imei": "354890871456823",
    "movil_id": "1880045712",
    "fecha": "2025-06-02",
    "hora": "08:15",
    "lat": "19.37234000",
    "lng": "-103.59123000",
    "latshort": "19.3723",
    "lonshort": "-103.5912",
    "economico": "COL-014",
    "crs": "0.00",
    "bateria": "13.62 v",
    "placas": "COL-014N",
    "spd": "0 km/h",
    "spd1": 0,
    "in_state": "00000000",
    "fix": "1",
    "signal_strength": "53",
    "ubi": "Pueblo Mágico de Comala, Comala, Col., Mexico",
    "title": "UNIDAD DETENIDA",
    "latshort2": "193723",
    "lonshort2": "103591",
    "fecha_equipo": "02/06/2025 08:15:06",
    "temp1": "31.8",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "789014"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 1 minuto(s) ",
    "imei": "354890871456824",
    "movil_id": "1880045713",
    "fecha": "2025-06-02",
    "hora": "08:16",
    "lat": "21.82567000",
    "lng": "-102.36789000",
    "latshort": "21.8256",
    "lonshort": "-102.3678",
    "economico": "AGS-015",
    "crs": "345.12",
    "bateria": "14.07 v",
    "placas": "AGS-015O",
    "spd": "55 Km/h",
    "spd1": 55,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "62",
    "ubi": "Libramiento Sur Poniente, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "218256",
    "lonshort2": "102367",
    "fecha_equipo": "02/06/2025 08:16:14",
    "temp1": "27.6",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "890123"
  },
  {
    "ultimo": "0 Día(s) 0 hora(s) 4 minuto(s) ",
    "imei": "354890871456825",
    "movil_id": "1880045714",
    "fecha": "2025-06-02",
    "hora": "08:13",
    "lat": "21.80123000",
    "lng": "-102.39456000",
    "latshort": "21.8012",
    "lonshort": "-102.3945",
    "economico": "AGS-015",
    "crs": "198.67",
    "bateria": "12.94 v",
    "placas": "AGS-015O",
    "spd": "37 Km/h",
    "spd1": 37,
    "in_state": "00000001",
    "fix": "1",
    "signal_strength": "49",
    "ubi": "Av. Siglo XXI 345, Aguascalientes, Ags., Mexico",
    "title": "UNIDAD EN MOVIMIENTO",
    "latshort2": "218012",
    "lonshort2": "102394",
    "fecha_equipo": "02/06/2025 08:13:59",
    "temp1": "26.3",
    "temp2": "0.0",
    "temp3": "0.0",
    "odometro": "890125"
  }
]
    return JSONResponse(content={"equipos": endpoints_list})
