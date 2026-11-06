#!/bin/bash
LOGFILE="$1"

if [ -f "$LOGFILE" ]; then
    PAYMENT=$(grep -c "ERROR PaymentService" "$LOGFILE")
    DB=$(grep -c "ERROR DBService" "$LOGFILE")
    ORDER=$(grep -c "ERROR OrderService" "$LOGFILE")
    echo "PaymentService: $PAYMENT"
    echo "DBService: $DB"
    echo "OrderService: $ORDER"
else
    echo "ERROR: $LOGFILE not found"
fi