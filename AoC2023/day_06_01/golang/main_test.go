package main

import (
	"os"
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestProblem(t *testing.T) {
	dat, _ := os.ReadFile("input.txt")
    assert.Equal(t, solve(string(dat)), "288")
}
