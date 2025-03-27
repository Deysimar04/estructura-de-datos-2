from typing import Union, Optional, Any, Dict, List
from fastapi import FastAPI, HTTPException
from practicaColas.model import Ticket
from practicaColas.controller import TicketController
from practicaColas.functions import add_queue

app = FastAPI()


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional["Node"] = None  


class Queue:
    def __init__(self):
        self.head: Optional[Node] = None  
        self.tail: Optional[Node] = None  

    def enqueue(self, item: Any) -> None:
        """Agrega un elemento al final de la cola."""
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def dequeue(self) -> Optional[Any]:
        """Elimina y devuelve el elemento al inicio de la cola."""
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return item


class TicketController:
    def __init__(self):
        self.queue: Queue = Queue()  

    def add_ticket(self, ticket: Any) -> None:
        """Agrega un ticket a la cola."""
        self.queue.enqueue(ticket)

    def get_next_ticket(self) -> Optional[Any]:
        """Obtiene el siguiente ticket en la cola."""
        return self.queue.dequeue()


ticketTypes: Dict[str, TicketController] = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}


@app.post("/ticketCreate")
def crear_turno(
    name: str,
    identity: str,
    type: str,
    age: int,
    priority: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Crea un nuevo turno y lo agrega a la cola correspondiente.
    """
    try:
        if type not in ticketTypes:
            raise HTTPException(status_code=400, detail="Tipo de atención no válido")
        if priority is None and age > 60:
            priority = True
        else:
            priority = False
        turno = Ticket(
            name=name,
            type=type,
            identity=identity,
            case_description="",
            age=age,
            priority_attention=priority
        )
        ticketTypes[type].add_ticket(turno)
        return {"mensaje": "Turno creado correctamente", "datos_turno": turno}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/ticketNext")
def obtener_siguiente_turno(type: str) -> Dict[str, Any]:
    """
    Devuelve el siguiente turno en la cola para el tipo de atención especificado.
    """
    if type not in ticketTypes:
        return {"mensaje": "Tipo de atención no válido"}
    
    next_ticket = ticketTypes[type].get_next_ticket()
    if next_ticket:
        return {"mensaje": "El siguiente turno es", "datos_turno": next_ticket}
    else:
        return {"mensaje": "No hay turnos en la cola"}


@app.get("/ticketList")
def listar_turnos_cola(type: str) -> Dict[str, Any]:
    """
    Lista todos los turnos pendientes en la cola para el tipo de atención especificado.
    """
    if type in ticketTypes:
        tickets: List[Any] = []
        current = ticketTypes[type].queue.head
        while current:
            tickets.append(current.data)
            current = current.next
        return {"mensaje": "Lista de turnos en cola", "datos_turnos": tickets}
    else:
        return {"mensaje": "Tipo de atención no válido"}


@app.get("/")
def read_root() -> Dict[str, str]:
    """
    Devuelve un mensaje de bienvenida.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None) -> Dict[str, Union[int, Optional[str]]]:
    """
    Devuelve información sobre un ítem específico.
    """
    return {"item_id": item_id, "q": q}
