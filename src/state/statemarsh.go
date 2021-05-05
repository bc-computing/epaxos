package state

import (
	"encoding/binary"
	"io"
)

func (t *Command) Marshal(w io.Writer) {
	var b [8]byte
	bs := b[:8]
	bs = b[:1]
	b[0] = byte(t.Op)
	w.Write(bs)
	bs = b[:8]
	
	//Changes made to accomandate experiment DataSize = 256B
	binary.LittleEndian.PutUint64(bs, uint64(t.K))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V1))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V2))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V3))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V4))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V5))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V6))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V7))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V8))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V9))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V10))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V11))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V12))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V13))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V14))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V15))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V16))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V17))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V18))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V19))
 	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V20))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V21))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V22))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V23))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V24))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V25))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V26))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V27))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V28))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V29))
 	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V30))
 	w.Write(bs)
 	binary.LittleEndian.PutUint64(bs, uint64(t.V31))
 	w.Write(bs)
	
	
}

func (t *Command) Unmarshal(r io.Reader) error {
	var b [8]byte
	bs := b[:8]
	bs = b[:1]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.Op = Operation(b[0])
	bs = b[:8]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V1 = Value(binary.LittleEndian.Uint64(bs))
	
	
	//Changes made to accomandate experiment DataSize = 256B	
	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V2 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V3 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V4 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V5 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V6 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V7 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V8 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V9 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V10 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V11 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V12 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V13 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V14 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V15 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V16 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V17 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V18 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V19 = Value(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V20 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V21 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V22 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V23 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V24 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V25 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V26 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V27 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V28 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V29 = Value(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
	t.V30 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
 	t.V31 = Value(binary.LittleEndian.Uint64(bs))
 	if _, err := io.ReadFull(r, bs); err != nil {
 		return err
 	}
	
	
	return nil
}

func (t *Key) Marshal(w io.Writer) {
	var b [8]byte
	bs := b[:8]
	binary.LittleEndian.PutUint64(bs, uint64(*t))
	w.Write(bs)
}

func (t *Value) Marshal(w io.Writer) {
	var b [8]byte
	bs := b[:8]
	binary.LittleEndian.PutUint64(bs, uint64(*t))
	w.Write(bs)
}

func (t *Key) Unmarshal(r io.Reader) error {
	var b [8]byte
	bs := b[:8]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	*t = Key(binary.LittleEndian.Uint64(bs))
	return nil
}

func (t *Value) Unmarshal(r io.Reader) error {
	var b [8]byte
	bs := b[:8]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	*t = Value(binary.LittleEndian.Uint64(bs))
	return nil
}
