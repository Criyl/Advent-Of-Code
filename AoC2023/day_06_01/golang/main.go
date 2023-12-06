package main

import (
	"os"
	"fmt"
	"regexp"
    "strconv"
	"strings"
)

type Race struct{
	time int
	distance int
}

func ingest_race(text string) []Race {
	re := regexp.MustCompile("\\s+") 
	lines := strings.Split(text, "\n")

	time_line := re.Split(lines[0], -1)
	distance_line := re.Split(lines[1], -1)
	
	var races []Race
	
	for i := 1; i < len(distance_line); i++{
		time, _ := strconv.Atoi(time_line[i])
		distance, _ :=strconv.Atoi(distance_line[i])
		race := Race{time,distance}
		races = append(races,race)
	}

	return races
}


func hold_button(hold_time int, race Race) int{
	return hold_time*(race.time - hold_time)
}

func solve(input string) string {
	races := ingest_race(input)

	result := 1
	for _, race := range races{
		won := 0
		for j := 0; j <= race.time; j++ {
			distance := hold_button(j, race)
			if distance > race.distance{
				won++
			}

		}
		if won > 0{
			result = result * won
		}
	}

	return strconv.Itoa(result)
}

func main() {
	dat, _ := os.ReadFile("input.txt")
	fmt.Println(solve(string(dat)))
}
