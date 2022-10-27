awk -F',' -v OFS=',' '
  NR == 1 {print "review_id", $0; next}
  {print (NR-1), $0}
' indeed_reviews_processed.csv > reviews_to_batch.csv