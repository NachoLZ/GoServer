package main

import (
	"fmt"
	"math/rand"
	"net"
	"strings"
	"time"
)

func random(min, max int) int {
	return rand.Intn(max-min) + min
}

func main() {

	PORT := ":50001"

	var jugadas [3]string
	jugadas[0] = "Piedra"
	jugadas[1] = "Papel"
	jugadas[2] = "Tijera"

	var jugada int
	var state int
	var statebool bool

	s, err := net.ResolveUDPAddr("udp4", PORT)
	if err != nil {
		fmt.Println(err)
		return
	}

	connection, err := net.ListenUDP("udp4", s)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer connection.Close()
	buffer := make([]byte, 1024)
	rand.Seed(time.Now().Unix())

	for {
		n, addr, err := connection.ReadFromUDP(buffer)
		fmt.Print("-> ", string(buffer[0:n-1]))

		state = random(1, 11)

		if strings.TrimSpace(string(buffer[0:n])) == "ready?" {
			if state > 8 {

				mensaje := []byte("NO")
				fmt.Printf("data: %s\n", string(mensaje))
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}
				statebool = false

			} else {
				mensaje := []byte("OK")
				fmt.Printf("data: %s\n", string(mensaje))
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}
				statebool = true

			}
		}

		if strings.TrimSpace(string(buffer[0:n])) == "jugada?" && statebool == true {
			jugada = random(0, 3)
			mensaje := []byte(jugadas[jugada])
			fmt.Printf("data: %s\n", string(mensaje))
			_, err = connection.WriteToUDP(mensaje, addr)
			if err != nil {
				fmt.Println(err)
				return
			}
		}

		if strings.TrimSpace(string(buffer[0:n])) == "STOP" {
			fmt.Println("Exiting UDP server!")
			return
		}

		//data := []byte(strconv.Itoa(random(1, 1001)))
		//fmt.Printf("data: %s\n", string(data))
		//_, err = connection.WriteToUDP(data, addr)
		//if err != nil {
		//	fmt.Println(err)
		//	return
		//}

	}
}
