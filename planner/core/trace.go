package core

import (
	"github.com/hanchuanchuan/tidb/ast"
)

// Trace represents a trace plan.
type Trace struct {
	baseSchemaProducer

	StmtNode ast.StmtNode
}
