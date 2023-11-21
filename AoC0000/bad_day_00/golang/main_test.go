package main

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestProblem(t *testing.T) {
    assert.Equal(t, solve("Test Case 1"), "Hello, Place")
}