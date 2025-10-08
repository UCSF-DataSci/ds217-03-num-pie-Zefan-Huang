#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    avg_heart_rate = np.mean(data['heart_rate'])
    avg_systolic_bp = np.mean(data['blood_pressure_systolic'])
    avg_glucose = np.mean(data['glucose_level'])
    stat = { 'avg_heart_rate': avg_heart_rate,
             'avg_systolic_bp': avg_systolic_bp,
             'avg_glucose': avg_glucose }
    for key in stat:
        stat[key] = float(f"{stat[key]:.1f}")
    return stat


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    high_hr_count = len(np.unique(data['patient_id'][data['heart_rate'] > 90])) ## first, use boolean mask to filter out heart rates, then apply to the current col, then use np.unique() to get unique values, finally use len() to count them
    high_bp_count = len(np.unique(data['patient_id'][data['blood_pressure_systolic'] > 130]))
    high_glucose_count = len(np.unique(data['patient_id'][data['glucose_level'] > 110]))
    stat = { 'high_heart_rate': high_hr_count,
             'high_blood_pressure': high_bp_count,
             'high_glucose': high_glucose_count }
    return stat


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    report = (f"Health Sensor Data Analysis Report\n"
            f"\nTotal Readings: {total_readings}\n"
            f"\nAverage Heart Rate: {stats['avg_heart_rate']:.1f} bpm\n"
            f"Systolic BP: {stats['avg_systolic_bp']:.1f} mmHg\n"
            f"Average Glucose Level: {stats['avg_glucose']:.1f} mg/dL\n"
            f"\nAbnormal Readings:\n"
            f"High Heart Rate (>90 bpm): {abnormal['high_heart_rate']}"
            f"\nHigh Blood Pressure (>130 mmHg): {abnormal['high_blood_pressure']}"
            f"\nHigh Glucose Level (>110 mg/dL): {abnormal['high_glucose']}\n"
    )
    return report



def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    f = open(filename, "w", encoding="utf-8")
    f.write(report)
    f.close()



def main():

    data = load_data("/Users/stefan/Desktop/Data Sci 217/ds217-03-num-pie-Zefan-Huang/health_data.csv")
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total_readings = len(data)
    report = generate_report(stats, abnormal, total_readings)
    save_report(report, "/Users/stefan/Desktop/Data Sci 217/ds217-03-num-pie-Zefan-Huang/output/analysis_report.txt")
    print("Analysis report saved to 'output/analysis_report.txt'")


if __name__ == "__main__":
    main()